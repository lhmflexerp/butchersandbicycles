# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = "res.partner"

    @api.multi
    @api.depends('property_product_pricelist')
    def _compute_set_custom_pricelist(self):
        for rec in self:
            rec.custom_pricelist_id = rec.property_product_pricelist.id
            
    custom_pricelist_id = fields.Many2one(
        'product.pricelist',
        string='Sale Pricelist',
        compute='_compute_set_custom_pricelist',
        store=True,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
