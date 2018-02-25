# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def write(self, values):
        res = super(MrpProduction, self).write(values)
        if values.get('date_planned_start', False):
            for rec in self:
                if rec.move_raw_ids:
                    rec.move_raw_ids.filtered(
                        lambda i: i.state not in ['done', 'cancel']).write({
                            'mrp_back_date': rec.date_planned_start
                        })

                if rec.move_finished_ids:
                    rec.move_finished_ids.filtered(
                        lambda i: i.state not in ['done', 'cancel']).write({
                            'mrp_back_date': rec.date_planned_start
                        })
        return res

    def _generate_finished_moves(self):
        move = super(MrpProduction, self)._generate_finished_moves()
        if move:
            move.write({'mrp_back_date': self.date_planned_start})
        return move

    def _generate_raw_move(self, bom_line, line_data):
        move = super(MrpProduction, self)._generate_raw_move(bom_line, line_data)
        if move:
            move.write({'mrp_back_date': self.date_planned_start})
        return move
