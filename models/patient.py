from odoo import models, fields, api
from datetime import date


# from datetime import time,datetime

class Hospital_managemnet(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital_managemnet"
    hospital_name = fields.Char(string="Hospital Name")
    name = fields.Char(string="Name", required=True)
    namedd = fields.Char(string="Name", required=True)
    name_two = fields.Many2one("hospital.medicine", string="Name", required=True)
    bod = fields.Date("BOD")
    active = fields.Boolean('Active', default=True)
    old_new = fields.Selection([("old", "OLD"), ("new", "new")], string="select")
    is_children = fields.Boolean(string="is_child")
    patientrecord = fields.Many2one('res.partner', string="patientrecord")
    peracitemol = fields.Many2many('hospital.medicine', "capsule_medic", "hospital_id", "medicine_id",
                                   string="peracitemol")
    relative_id = fields.Many2one("hospital.department", string="tokyo")
    patient_id = fields.Many2one("res.partner", string="pationt",domain=[("mobile","=",'yashuuuuuuuuudan')])
    SpecialCommand = fields.Char(string="patient", required=True)
    gender = fields.Selection([("male", "MALE"), ("female", "FEMALE"), ("other", "OTHER")], string="gender")
    age = fields.Integer(string="age" )
    gun = fields.Char(string="HELlo")


    def ggggggggg(self):
        self.update({
            # 'peracitemol': [(fields.Command.create({"name": "kumfu"}))]
            # 'peracitemol': [(fields.Command.update(24,{"name":"jordar"}))]
            # 'peracitemol': [(fields.Command.delete(24))]
            'peracitemol': [(fields.Command.clear())]
        })
    # def H_Name(self):
    #     self.hospital_name = "****Zydus Hospital*****"
    # @api.depends("old_new")
    # def _compute_age(self):
    #     self.age = 10

    @api.onchange('name_two')
    def onchange_name_two(self):
        if self.name_two:
            if self.name_two.gender:
                self.gender = self.name_two.gender

    # @api.model
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         # print("------------------------------------------------>",record)
    #         name = record.hospital_name
    #         # print("------------------------------------------------>",name)
    #         # print("------------------------------------------------>",record.namedd)
    #         if record.name:
    #             name = record.namedd + name
    #             # print("------------------------------------------------>",name)
    #         res.append((record.id, name))
    #     # print("------------------------------------------------>",res)
    #     return res

    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     # print(".----------------------->", args)
    #     # print(".----------------------->", operator)
    #     # print(".----------------------->", limit)
    #     ids = self._name_search(name, args, operator, limit=limit)
    #     # print(".----------------------->", name)
    #     # print(".----------------------->",ids)
    #     return self.browse(ids).sudo().name_get()
    #
    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     print(".----------------------->", args)
    #     print(".----------------------->", operator)
    #     print(".----------------------->", limit)
    #     print(".----------------------->", name)
    #     print(".----------------------->", name_get_uid)
    #     if name:
    #         # Be sure name_search is symetric to name_get
    #         name = name.split(' / ')[-1]
    #         print(".----------------------->", name)
    #         args = [('name', operator, name)] + args
    #         print(".----------------------->", args)
    #     print(self._search(args, limit=limit, access_rights_uid=name_get_uid))
    #     return self._search(args, limit=limit, access_rights_uid=name_get_uid) @ api.model

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        print("self------------------------------------------------------------>", self)
        print("arge------------------------------------------------------------>", args)
        domain = []
        if name:
            print("name------------------------------------------------------------>", name)
            domain = ['|', ('namedd', operator, name), ('old_new', operator, name)]
            print("domain1------------------------------------------------------------>", domain)
        print("domain2------------------------------------------------------------>", domain)
        print("return------------------------------------------------------------>",
              self._search(domain + args, limit=limit, access_rights_uid=name_get_uid))
        print("domain+arge---------------------->", domain + args)
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    
