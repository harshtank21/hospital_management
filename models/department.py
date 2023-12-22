from odoo import models, fields, api


class Hospital_department(models.Model):
    _name = "hospital.department"
    _description = "Hospital_department"
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="age")
    time = fields.Selection(
        [("11:00", "11:00"), ("12:00", "12:00"), ("1:00", "1:00"), ("2:00", "2:00"), ("3:00", "3:00")], string="select")
    # is_balak=fields.Boolean(string="is balak")
    relatives_ids = fields.One2many("hospital.hospital", "relative_id", string="relatives")
    patient_count = fields.Integer(string="Patient count")

    new_one = fields.Many2one("hospital.hospital", string="new_one")
