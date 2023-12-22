from odoo import models,fields,api

class Hospital_medicine(models.Model):
    _name = "hospital.medicine"
    _description = "Hospital_department"
    name = fields.Char(string="Name", required=True)
    age=fields.Integer(string="Age")
    add_img=fields.Binary(string="Add_Img")
    type=fields.Selection([("general sales list","GENERAL SALES LIST"),("pharmacy only","PHARMACY ONLY"),("herbal medicines","HERBAL MEDICINES"),("Prescription only medication","Prescription only medication")],string="Type")
    medicine=fields.Char(string="Medicine Name")
    made=fields.Many2one("hospital.hospital",string="made")
    # peracitemol=fields.Many2many('hospital.hospital',"capsule_medicine","hospital_id","medicine_id",string="peracitemol")
    gender=fields.Selection([("male","MALE"),("female","FEMALE"),("other","OTHER")],string="gender")



    pai=fields.Many2one("hospital.hospital",string="onehospital")
    paione=fields.Many2one("hospital.department",
                           string="diphospital",
                           domain=[("paione",'=','pai.id')])

    def object_test(self):
        print("button_click______________________________________________________")




