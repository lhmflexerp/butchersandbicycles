# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class PaymentTerm(models.Model):
    _inherit = "account.payment.term"

    date_from_so_request_date = fields.Boolean(
        string='Based on Sales Order Date?',
        copy=False,
        help='Tick this box if you want to consider date of sales order instead of invoice date.',
    )

    @api.one#fully override
    def compute(self, value, date_ref=False):
        date_ref = date_ref or fields.Date.today()

        # patch #below part important.
        if self.date_from_so_request_date:
            ctx = self._context
            params = ctx.get('params', {})
            if params.get('model', '') == 'sale.order' and ctx.get('type', '') == 'out_invoice':
                order = self.env['sale.order'].sudo().browse(ctx['active_id'])
                if order.requested_date:
                    date_ref = order.requested_date

        amount = value
        sign = value < 0 and -1 or 1
        result = []
        if self.env.context.get('currency_id'):
            currency = self.env['res.currency'].browse(self.env.context['currency_id'])
        else:
            currency = self.env.user.company_id.currency_id
        for line in self.line_ids:
            if line.value == 'fixed':
                amt = sign * currency.round(line.value_amount)
            elif line.value == 'percent':
                amt = currency.round(value * (line.value_amount / 100.0))
            elif line.value == 'balance':
                amt = currency.round(amount)
            if amt:
                next_date = fields.Date.from_string(date_ref)
                if line.option == 'day_after_invoice_date':
                    next_date += relativedelta(days=line.days)
                elif line.option == 'fix_day_following_month':
                    next_first_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                    next_date = next_first_date + relativedelta(days=line.days - 1)
                elif line.option == 'last_day_following_month':
                    next_date += relativedelta(day=31, months=1)  # Getting last day of next month
                elif line.option == 'last_day_current_month':
                    next_date += relativedelta(day=31, months=0)  # Getting last day of next month
                result.append((fields.Date.to_string(next_date), amt))
                amount -= amt
        amount = sum(amt for _, amt in result)
        dist = currency.round(value - amount)
        if dist:
            last_date = result and result[-1][0] or fields.Date.today()
            result.append((last_date, dist))

        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
