from odoo import models, fields, api


class sale_order(models.Model):
    _inherit = "sale.order"

    manufacture_date = fields.Char(string="manu")


# class sale_order_ONE(models.Model):
#     _inherit = "product.template"
#
#     unique = fields.Char(string="Unique Code")

    @api.model
    def _name_search(self, name="", args=None, operator='like', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        domain = [('categ_id.office_furniture', operator, True)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    # @api.model
    # def name_get(self):
    #
    #     res = []
    #     for record in self:
    #         name = record.name
    #         if record.default_code != False:
    #             if record.categ_id.office_furniture == True:
    #                 name = "[ABC_" + record.default_code + "]" + name
    #             res.append((record.id, name))
    #     return res


class qunt_one(models.Model):
    _inherit = "stock.quant"


class Sale_Order_New(models.Model):
    _inherit = "sale.order.line"

    on_hand = fields.Char(string="ON Heand qty", compute="_compute_on_hand_quantity_count")

    @api.depends('product_id')
    def _compute_on_hand_quantity_count(self):
        for rec in self:
            # max=rec.product_id.mapped(
            #     "stock_quant_ids"
            # ).filtered(
            #     lambda quant: quant.location_id.usage == 'internal'
            # )
            # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",max)
            rec.on_hand = rec.product_id.mapped("additional_product_tag_ids").filtered(
                lambda x: len(x.name) == len(x.name)).mapped("write_uid").name
            print("---------------------------->", rec.on_hand)
            # qty_lst = rec.product_id.mapped(
            #     "stock_quant_ids"
            # ).filtered(
            #     lambda quant: quant.location_id.usage == 'internal'
            # ).mapped(
            #     "quantity"
            # )
            # print("\n\n\n\n\n\n\n\n\n\n", qty_lst)
            # rec.on_hand = sum(
            #     qty_lst
            # ) if qty_lst else 0

            #
            # qty = 0
            # for prod in rec.product_id:
            #     for quant in prod.stock_quant_ids:
            #         qty += quant.qty if quant.location_id.usage == '' else 0

    #     # self.c=list(filter(lambda x : x.product_id.stock_quant_ids.location_id.usage == "Internal Location",self))
    #         # if (rec.product_id.stock_quant_ids.location_id.usage == "Internal Location"):
    #         rec= list(filter(lambda x: x.product_id.stock_quant_ids.location_id.usage == "Internal Location",rec))

    # for val in product:
    #         val.total_one = val.quantity


class product_tempalet(models.Model):
    _inherit = "product.category"

    office_furniture = fields.Boolean(string="Office furniture")
    # @api.model
    # def _name_search(self, name="", args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         print("hello")
    #         domain = [('name', operator, 'Office Furniture')]
    #         # domain = [('categ_id', operator, "Office Furniture"), ("name", operator, name)]
    #     return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
