from odoo import models,fields
from datetime import time,datetime

class Hospital_managemnet(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital_managemnet"
    name=fields.Char(string="Name", required=True)
    age=fields.Integer(string="age")
    old_new=fields.Selection([("old","OLD"),("new","new")],string="select")
    is_balak=fields.Boolean(string="is balak")
