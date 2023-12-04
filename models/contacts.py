from odoo import models,fields
class Contacts(models.Model):
    _inherit ='res.partner'

    patient_entry_ids=fields.One2many("hospital.hospital","patient_id",string="Patient Entry")
    patient_entry=fields.Char(string="patient_entry")
