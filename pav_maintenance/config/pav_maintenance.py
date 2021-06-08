from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Service Center"),
			"items": [
				{
					"type": "doctype",
					"name": "Operation Order",
					"description":_("Operation Order"),
					"onboard": 1					
				},				
			]
		},
		{
			"label": _("Report"),
			"items": [				
			]
		},

		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Service Center Settings",
					"description":_("Service Center Settings")
				},
				{
					"type": "doctype",
					"name": "Model",
					"description":_("Model")
				},
				{
					"type": "doctype",
					"name": "Software Versions",
					"description":_("Software Versions")
				},
				{
					"type": "doctype",
					"name": "Replacement Reason",
					"description":_("Replacement Reason")
				},
				{
					"type": "doctype",
					"name": "Device Accessory",
					"description":_("Device Accessory")
				}
			]
		},
		{
			"label": _("Malfunction"),
			"items": [
				{
					"type": "doctype",
					"name": "Malfunction",
					"description":_("Malfunction")
				},
				{
					"type": "doctype",
					"name": "Common Malfunction",
					"description":_("Common Malfunction")
				},
				{
					"type": "doctype",
					"name": "Malfunction Type",
					"description":_("Malfunction Type")
				},
				{
					"type": "doctype",
					"name": "Malfunctions Group",
					"description":_("Malfunctions Group")
				},
			]
		},
		{
			"label": _("Engineer and Maintenance Workshop"),
			"items": [
				{
					"type": "doctype",
					"name": "Engineer",
					"description":_("Engineer")
				},	
				{
					"type": "doctype",
					"name": "Maintenance Workshop",
					"description":_("Maintenance Workshop")
				}				
			]
		},
		{
			"label": _("Consumer"),
			"items": [
				{
					"type": "doctype",
					"name": "Consumer",
					"description":_("Consumer")
				},
				{
					"type": "doctype",
					"name": "Consumer Group",
					"description":_("Consumer Group")
				},	
				{
					"type": "doctype",
					"name": "Contact",
					"description":_("Contact")
				},
				{
					"type": "doctype",
					"name": "Address",
					"description":_("Address")
				},								
			]
		},
	]