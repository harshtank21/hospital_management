from odoo import models, fields, api


class Contacts(models.Model):
    _inherit = 'res.partner'

    patient_entry_ids = fields.One2many("hospital.hospital", "patient_id", string="Patient Entry")
    patient_entry = fields.Char(string="patient_entry")
    patient_enftry = fields.Char(string="patient_entry")
    gender = fields.Selection([("male", 'Male'), ('female', 'Female')])




class Gender(models.Model):
    _inherit = "product.template"

    gender = fields.Selection([("male", 'Male'), ('female', 'Female')])
    @api.model
    def _name_search(self, name="", args=None, operator='like', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        domain = [('gender', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)


# def write(self, vals):
#     print(vals)
#     # vals["patient_enftry"] = vals["phone"]
#     print(self)
#     print(vals)
#     print(super(Contacts, self).write(vals))
#     vals["patient_enftry"] = self.phone
#     res = super(Contacts, self).write(vals)
#     print(self.phone + self.email, "----------------------------------------------------------<")
#     print(res, "----------------------------------------------------------<")
#     # res.patient_enftry = res.phone + res.email
#     print(self.email, "----------------------------------------------------------<")
#     print(self.phone, "----------------------------------------------------------<")
#     return res
#
#
# @api.model
#
#
# def create(self, vals):
#     print(vals)
#     print(self)
#     # print(self.phone + self.email, "----------------------------------------------------------<")
#
#     vals["patient_enftry"] = vals["phone"] + vals["email"]
#     res = super(Contacts, self).create(vals)
#     print(res, "----------------------------------------------------------<")
#     return res
