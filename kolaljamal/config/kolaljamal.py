from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Report"),
			"items": [
				{
					"type": "report",
					"name": "Salesman Itemwise Commission",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				}
			]
		}
	]
