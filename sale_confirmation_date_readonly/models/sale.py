# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmation_date = fields.Datetime(
        readonly=False, 
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
