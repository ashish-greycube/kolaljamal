# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "kolaljamal"
app_title = "Kolaljamal"
app_publisher = "GreyCube Technologies"
app_description = "Customization for kolaljamal"
app_icon = "fa fa-modx"
app_color = "green"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kolaljamal/css/kolaljamal.css"
# app_include_js = "/assets/kolaljamal/js/kolaljamal.js"

# include js, css files in header of web template
# web_include_css = "/assets/kolaljamal/css/kolaljamal.css"
# web_include_js = "/assets/kolaljamal/js/kolaljamal.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice": "public/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "kolaljamal.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kolaljamal.install.before_install"
# after_install = "kolaljamal.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kolaljamal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kolaljamal.tasks.all"
# 	],
# 	"daily": [
# 		"kolaljamal.tasks.daily"
# 	],
# 	"hourly": [
# 		"kolaljamal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kolaljamal.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kolaljamal.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kolaljamal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kolaljamal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "kolaljamal.task.get_dashboard_data"
# }
