# -*- coding: utf-8 -*-

from openerp import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    @api.depends(
        'picking_id.date_done',
        'date',
        'mrp_back_date'
    )
    def compute_back_date(self):
        res = super(StockMove, self).compute_back_date()
        for rec in self:

            if rec.picking_id.back_date:
                rec.back_date = rec.picking_id.back_date
            elif rec.mrp_back_date:
                rec.back_date = rec.mrp_back_date
            else:
                rec.back_date = rec.date
        return res

    mrp_back_date = fields.Datetime(
       'Back Date (MRP)', 
       help="back_date from MRP",
       readonly=True,
       copy=False,
    )

    @api.multi
    def _action_done(self):
        stock_moves = super(StockMove, self)._action_done()
        for move in stock_moves:
            if move.mrp_back_date:
                move.move_line_ids.write({
                    'mrp_back_date': move.mrp_back_date
                })
        return stock_moves

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    mrp_back_date = fields.Datetime(
       'Back Date (MRP)', 
       help="Back Date from MRP",
       readonly=True,
       copy=False,
    )
