from odoo import models, fields , api
from datetime import date


# from datetime import time,datetime

class Hospital_managemnet(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital_managemnet"
    hospital_name = fields.Char(string="Hospital Name")
    name = fields.Char(string="Name", required=True)
    namedd = fields.Char(string="Name", required=True)
    name_two=fields.Many2one("hospital.medicine",string="Name", required=True)
    bod=fields.Date("BOD")
    old_new = fields.Selection([("old", "OLD"), ("new", "new")], string="select")
    # is_child = fields.Char(string="is_child", compute='sem')
    is_children = fields.Boolean(string="is_child")
    patientrecord = fields.Many2one('res.partner', string="patientrecord")
    peracitemol = fields.Many2many('hospital.medicine', "capsule_medic", "hospital_id", "medicine_id",
                                   string="peracitemol")
    relative_id = fields.Many2one("hospital.department", string="tokyo")
    patient_id = fields.Many2one("res.partner", string="pationt")
    SpecialCommand = fields.Char(string="patient", required=True)
    gender=fields.Selection([("male","MALE"),("female","FEMALE"),("other","OTHER")],string="gender")
    age = fields.Integer(string="age",compute="_compute_age")

    # def H_Name(self):
    #     self.hospital_name = "****Zydus Hospital*****"

    def _compute_age(self):
        for i in self:
            print(i)
            today=date.today()
            print(today)
            if i.bod:
                i.age=today.year-i.bod.year
                print(i.age)
            else:
                i.age=0

    @api.onchange('name_two')
    def onchange_name_two(self):
        if self.name_two:
            if self.name_two.gender:
                self.gender=self.name_two.gender


    # def name_get(self,k):
    #     res = []
    #     for record in self:
    #         print("------------------------------------------------>",record)
    #         name = record.hospital_name
    #         print("------------------------------------------------>",name)
    #         print("------------------------------------------------>",record.namedd)
    #         if record.name:
    #             name ='[' + record.namedd + ']' + name
    #             print("------------------------------------------------>",name)
    #         res.append((record.id, name))
    #     print("------------------------------------------------>",res)
    #     return res
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):

        print(".----------------------->", args)
        print(".----------------------->", operator)
        print(".----------------------->", limit)
        print(".----------------------->", name)
        ids = self._name_search(name, args, operator, limit=limit)
        print(".----------------------->",ids)
        return self.browse(ids).sudo().name_get()

