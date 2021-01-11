# Copyright (c) 2013, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
    columns, data = [], []
    return get_columns(), get_data(filters)


def get_columns():
    return [
        dict(
            label="InvoiceNo",
            fieldname="invoice_no",
            fieldtype="Link",
            options="Sales Invoice",
            width=150,
        ),
        dict(label="Date", fieldname="posting_date", fieldtype="Date", width=120),
        dict(label="Item Name", fieldname="item_name", fieldtype="Data", width=150),
        dict(
            label="Item Code/Item",
            fieldname="item_code",
            fieldtype="Link/Item",
            width=150,
        ),
        dict(
            label="Sales Amount",
            fieldname="base_net_total",
            fieldtype="Currency",
            width=130,
        ),
        dict(
            label="Salesman Commission",
            fieldname="salesman_commission",
            fieldtype="Currency",
            width=150,
        ),
        dict(
            label="Supervisor Commission",
            fieldname="supervisor_commission",
            fieldtype="Currency",
            width=150,
        ),
        dict(
            label="Manager Commission",
            fieldname="manager_commission",
            fieldtype="Currency",
            width=150,
        ),
    ]


def get_data(filters):
    conditions = []
    user = frappe.session.user

    if not user == "Administrator":
        sales_person = frappe.db.get_values(
            "Sales Person",
            {"sales_user_id_cf": user},
            ["name", "sales_person_type_cf"],
            as_dict=True,
        )
        if not sales_person:
            return []
        sales_person = sales_person[0]
        print(sales_person)

        if sales_person.sales_person_type_cf == "Manager":
            filters["manager"] = sales_person.name
        elif sales_person.sales_person_type_cf == "Supervisor":
            filters["supervisor"] = sales_person.name
        elif sales_person.sales_person_type_cf == "Salesman":
            filters["salesman"] = sales_person.name
        else:
            conditions += ["0=1"]

    if filters.get("from_date"):
        conditions += ["si.posting_date >= %(from_date)s "]
    if filters.get("to_date"):
        conditions += ["si.posting_date <= %(to_date)s "]
    if filters.get("salesman"):
        conditions += ["si.salesman_cf = %(salesman)s "]
    if filters.get("supervisor"):
        conditions += [
            """
        si.salesman_cf in 
        (
            select a.name 
            from `tabSales Person` a
            inner join `tabSales Person` b 
            on b.name = %(supervisor)s
            and a.lft > b.lft and a.rgt < b.rgt
        )"""
        ]
    if filters.get("manager"):
        conditions += [
            """
        si.salesman_cf in 
        (
            select a.name 
            from `tabSales Person` a
            inner join `tabSales Person` b 
            on b.name = %(manager)s 
            and a.lft > b.lft and a.rgt < b.rgt
        )"""
        ]

    conditions = conditions and " where " + " and ".join(conditions) or ""

    return frappe.db.sql(
        """
    select
        si.name as invoice_no,
        si.posting_date,
        sit.item_name,
        sit.item_code,
        si.base_net_total,
        ti.salesman_commission_cf*base_net_total/100 as salesman_commission,
        ti.supervisor_commission_cf*base_net_total/100 as supervisor_commission,
        ti.manager_commission_cf*base_net_total/100 as manager_commission
    from 
        `tabSales Invoice` as si
        inner join `tabSales Invoice Item` as sit
        on  si.name = sit.parent
        and si.docstatus = 1
        inner join `tabItem` as ti
        on sit.item_code = ti.item_code
        {conditions}
    """.format(
            conditions=conditions
        ),
        filters,
        as_dict=True,
        debug=0,
    )
