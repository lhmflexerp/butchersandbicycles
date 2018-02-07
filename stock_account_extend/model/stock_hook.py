# -*- coding: utf-8 -*-

from collections import defaultdict

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round

import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"
    
    def _create_stock_move(self, journal_id, move_lines, date, move):#hook
        AccountMove = self.env['account.move']
        
        date_pick = date
        if not move.picking_id.date_done:
            pass
        if move.picking_id and move.picking_id.date_done:
            date_pick = move.picking_id.date_done
        elif move.date_adjustment:
            date_pick = move.date_adjustment
        elif move.back_date:
            date_pick = move.back_date



        new_account_move = AccountMove.create({
                    'journal_id': journal_id,
                    'line_ids': move_lines,
                    'date': date_pick,#
                    'ref': move.picking_id.name})
        return new_account_move

