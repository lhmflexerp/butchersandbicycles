# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockQuantityHistory(models.TransientModel):
    _inherit = 'stock.quantity.history'

    def open_table(self):
        self.ensure_one()

        if self.compute_at_date:
            tree_view_id = self.env.ref('stock.view_stock_product_tree').id
            form_view_id = self.env.ref('stock.product_form_view_procurement_button').id
            # We pass `to_date` in the context so that `qty_available` will be computed across
            # moves until date.
            action = {
                'type': 'ir.actions.act_window',
                'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
                'view_mode': 'tree,form',
                'name': _('Products'),
                'res_model': 'product.product',
                'context': dict(self.env.context, to_date=self.date, special= True),  # (Pass a special context.)
            }
            return action
        else:
            self.env['stock.quant']._merge_quants()
            return self.env.ref('stock.quantsact').read()[0]
