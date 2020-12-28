frappe.ui.form.on("Sales Invoice", {
  onload: function (frm) {
    frm.set_query("salesman_cf", function () {
      return {
        filters: {
          sales_person_type_cf: "Salesman",
        },
      };
    });
  },
});
