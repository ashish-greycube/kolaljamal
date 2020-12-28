// Copyright (c) 2016, GreyCube Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Salesman Itemwise Commission"] = {
  filters: [
    {
      fieldname: "from_date",
      label: __("From"),
      fieldtype: "Date",
      default: frappe.datetime.month_start(),
      reqd: 1,
    },
    {
      fieldname: "to_date",
      label: __("To"),
      fieldtype: "Date",
      default: frappe.datetime.month_end(),
      reqd: 1,
    },
    {
      fieldname: "manager",
      label: __("Manager"),
      fieldtype: "Link",
      options: "Sales Person",
      get_query: () => {
        return {
          filters: { sales_person_type_cf: "Manager" },
        };
      },
      reqd: 0,
    },
    {
      fieldname: "supervisor",
      label: __("Supervisor"),
      fieldtype: "Link",
      options: "Sales Person",
      get_query: () => {
        return {
          filters: { sales_person_type_cf: "Supervisor" },
        };
      },
      reqd: 0,
    },
    {
      fieldname: "salesman",
      label: __("Salesman"),
      fieldtype: "Link",
      options: "Sales Person",
      get_query: () => {
        return {
          filters: { sales_person_type_cf: "Salesman" },
        };
      },
      reqd: 0,
    },
  ],
};
