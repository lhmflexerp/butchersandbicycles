# -*- coding: utf-8 -*-

# Part of Alex Lyngse. See LICENSE file for full copyright and licensing details.

{
    'name': "Payment Term _ Due Date Based on Sales Date",
    'version': '1.0',
    'category': 'Sales',
    'license': 'Other proprietary',
    'summary': """Due Date Calculation Using Sale Order Request Date""",
    'description': """
Invoice Due Date From Sale Order based on payment term.
We have som special payment terms:
100% payment due 5 working days before shipping date

We need to be able to calculate and set the due date on invoices accourding to the shippingdate on the SO.

We already have the field, custom_sale_id on invoice, wich create a link to the salesorder.

On the sale.order we have the field, requested_date

So, we need to be able to create a payment term, wich will calculate the duedate from  sale.order.requested date instead of invoice date.

currently odoo is considering Invoice date in all places where date due is available. Like on invoice form "Due date" and when we validate invoice while creating journal items which has due date which is also calculated by considering invoice date... Do you want to change invoice date to sale.order request date in call places? 

 i want to change to sale.order request date, but only on selected payment terms. So, i gues we will have to put a boolean field, "Date from SO request date", on payment terms 
""",
    'author': 'Alex Lyngse',
    'website': "",
    'depends': [
        'sale_order_dates',
    ],
    'data':[
        'views/payment_term_view.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
