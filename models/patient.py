from odoo import models, fields


# from datetime import time,datetime

class Hospital_managemnet(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital_managemnet"
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="age")
    old_new = fields.Selection([("old", "OLD"), ("new", "new")], string="select")
    is_child = fields.Boolean(string="is_child")
    patientrecord = fields.Many2one('res.partner', string="patientrecord")
    peracitemol = fields.Many2many('hospital.medicine', "capsule_medic", "hospital_id", "medicine_id", string="peracitemol")
    relative_id=fields.Many2one("hospital.department",string="tokyo")
    patient_id=fields.Many2one("res.partner",string="pationt")