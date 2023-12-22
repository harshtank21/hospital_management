from odoo import models, fields, api


class sale_order(models.Model):
    _inherit = "sale.order"

    manufacture_date = fields.Char(string="manu")


class sale_order_ONE(models.Model):
    _inherit = "product.template"

    unique = fields.Char(string="Unique Code")


class qunt_one(models.Model):
    _inherit = "stock.quant"


class Sale_Order_New(models.Model):
    _inherit = "sale.order.line"

    on_hand = fields.Float(string="ON Heand qty", compute="_compute_on_hand_quantity_count")

    # on_hand = fields.Float(string="ON Heand qty")

    #     for rec in self:
    @api.depends('product_id')
    def _compute_on_hand_quantity_count(self):
        for rec in self:
            qty_lst = list(rec.product_id.mapped(
                "stock_quant_ids"
            ).filtered(
                lambda quant: quant.location_id.usage == 'Internal Location'
            ).mapped(
                "quant_ids"
            ).quantity
                           )
            print("\n\n\n\n\n\n\n\n\n\n", qty_lst)
            rec.on_hand = sum(
                qty_lst
            ) if qty_lst else 0

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
