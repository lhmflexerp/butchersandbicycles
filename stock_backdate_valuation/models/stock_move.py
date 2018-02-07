# -*- coding: utf-8 -*-

import datetime
from openerp import models, fields, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    back_date = fields.Datetime(
       'Back Date (Stock Move Line)', 
#        default=fields.Datetime.now, 
       required=False,
       states={'done': [('readonly', True)]},
       help="back_date from stock move and picking"
    )

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    @api.depends('picking_id.date_done', 'date')
    def compute_back_date(self):
        for rec in self:
            #if rec.picking_id.date_done:
            #    rec.back_date = rec.picking_id.date_done
            if rec.picking_id.back_date:
                rec.back_date = rec.picking_id.back_date
            else:
                rec.back_date = rec.date

    back_date = fields.Datetime(
        string='Back Date',
        compute='compute_back_date',
        store=True
    )
    
    @api.multi
    def _action_done(self):
        moves_todo = super(StockMove, self)._action_done()
        for sm in moves_todo:
            if sm.back_date:
                sm.write({'date': sm.back_date})
                for move_line_st in sm.move_line_ids:
                    move_line_st.back_date = sm.back_date
                    move_line_st.date = sm.back_date
        return moves_todo

class StockPick(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_done(self):
        res = super(StockPick, self).action_done()
        for pick in self:
            if pick.back_date:
                pick.date_done = pick.back_date


    back_date = fields.Datetime(
        string='Back Date',
    )
