# -*- coding: utf-8 -*-

# Part of Alex Lyngsøe. See LICENSE file for full copyright and licensing details.

{
    'name': "Customer Pricelist Group by",
    'version': '1.0',
    'category': 'Sales',
    'license': 'Other proprietary',
    'summary': """Custom field for group by customer sale pricelist""",
    'description': """
    Customer Pricelist Groupby
    
    Customer group by
    """,
    'author': 'Alex Lyngsøe',
    'website': "www.odoo.com",
    'depends': [
        'product',
    ],
    'data':[
        'views/partner_view.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
