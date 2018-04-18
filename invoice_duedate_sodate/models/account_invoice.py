# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('payment_term_id', 'date_invoice')
    def _onchange_payment_term_date_invoice(self):
        ctx = self._context.copy()
        ctx.update(custom_sale_id=self.custom_sale_id.id)
        return super(
            AccountInvoice, self.with_context(ctx)
        )._onchange_payment_term_date_invoice()

    @api.multi
    def action_invoice_open(self):
        ctx = self._context.copy()
        if len(self) == 1:
            ctx.update(custom_sale_id=self.custom_sale_id.id)
        return super(
            AccountInvoice, self.with_context(ctx)
        ).action_invoice_open()
