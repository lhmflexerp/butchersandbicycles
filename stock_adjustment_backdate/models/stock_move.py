# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    date_adjustment = fields.Datetime(
       'Date Adjustment (Stock Move Line)', 
#        default=fields.Datetime.now, 
       required=False,
       states={'done': [('readonly', True)]},
       help="Move date: scheduled date until move is done, then date of actual move processing"
    )
  

class StockMove(models.Model):
    _inherit = "stock.move"

    date_adjustment = fields.Datetime(
       'Date Adjustment', 
#        default=fields.Datetime.now, 
       required=False,
       states={'done': [('readonly', True)]},
       help="Move date: scheduled date until move is done, then date of actual move processing"
    )
    
    @api.multi
    def _action_done(self):
        moves_todo = super(StockMove, self)._action_done()
        for sm in moves_todo:
            if sm.date_adjustment:
                sm.write({'date': sm.date_adjustment})
                for move_line_st in sm.move_line_ids:
                    move_line_st.date_adjustment = sm.date_adjustment
                    move_line_st.date = sm.date_adjustment
        return moves_todo

#     @api.multi
#     def action_done(self):
#         res = super(StockMove, self).action_done()
#         for rec in self:
#             self.write({'date': rec.date_adjustment})
#         return res