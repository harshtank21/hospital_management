from odoo import models, fields


# from datetime import time,datetime

class Hospital_managemnet(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital_managemnet"
    hospital_name = fields.Char(string="Hospital Name", compute='H_Name')
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="age")
    old_new = fields.Selection([("old", "OLD"), ("new", "new")], string="select")
    # is_child = fields.Char(string="is_child", compute='sem')
    is_children = fields.Boolean(string="is_child")
    patientrecord = fields.Many2one('res.partner', string="patientrecord")
    peracitemol = fields.Many2many('hospital.medicine', "capsule_medic", "hospital_id", "medicine_id",
                                   string="peracitemol")
    relative_id = fields.Many2one("hospital.department", string="tokyo")
    patient_id = fields.Many2one("res.partner", string="pationt")
    SpecialCommand = fields.Char(string="patient", required=True)

    def H_Name(self):
        self.hospital_name = "****Zydus Hospital*****"