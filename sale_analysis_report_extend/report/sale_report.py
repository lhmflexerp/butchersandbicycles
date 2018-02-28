# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    state_id = fields.Many2one(
        'res.country.state',
        string="Partner State",
    )
    requested_date = fields.Datetime(
        string='Expected shipping date',
    )

    def _select(self):
        select_str = super(SaleReport, self)._select()
        select_str += ",s.state_id as state_id"
        select_str += ",s.requested_date as requested_date"
        return select_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ",s.state_id"
        group_by_str += ",s.requested_date"
        return group_by_str

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
