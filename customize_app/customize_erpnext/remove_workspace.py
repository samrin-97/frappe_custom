import frappe

"""
bench --site limit.com execute customize_app.customize_erpnext.remove_workspace.remove_workspace
"""

def remove_workspace():
    frappe.db.sql('DELETE FROM tabWorkspace WHERE name NOT IN("HR","Payroll")')

