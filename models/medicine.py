from odoo import models,fields

class Hospital_medicine(models.Model):
    _name = "hospital.medicine"
    _description = "Hospital_department"
    name = fields.Char(string="Name", required=True)

    # is_balak=fields.Boolean(string="is balak")