# -*- coding: utf-8 -*-
# Copyright (c) 2021, Partner Team and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class OperationOrder(Document):
	pass

@frappe.whitelist()
def make_material_request(source_name, target_doc=None):
	visit = frappe.db.sql("""select t1.name
		from `tabMaterial Request` t1, `tabMaterial Request Item` t2
		where t2.parent=t1.name and t2.prevdoc_docname=%s""", source_name)

	if not visit:
		doclist = get_mapped_doc("Operation Order", source_name, {
			"Operation Order": {
				"doctype": "Material Request",
				"validation": {
					"docstatus": ["=", 0]
				}
			},
			"Operation Order Item": {
				"doctype": "Material Request Item",
				"field_map": {
					"parent": "prevdoc_docname",
					"parenttype": "prevdoc_doctype"
				},
				"add_if_empty": True
			}
		}, target_doc)

		return doclist