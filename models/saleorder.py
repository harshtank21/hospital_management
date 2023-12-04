from odoo import models, fields



class sale_order(models.Model):
    _inherit = "sale.order"

    manufacture_date=fields.Char(string="manu")