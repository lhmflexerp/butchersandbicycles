# -*- coding: utf-8 -*-

{
    'name' : 'Back Date For MRP',
    'version' : '1.0',
    'category': 'Manufacturing',
    'author': 'Alex Lyngse',
    'website': 'www.odoo.com',
    'description': """
    Added Back Date for MRP and its move and move lines.
""",
    'summary' : 'Back Date For MRP',
    'depends' : [
        'stock_backdate_valuation',
        'mrp',
    ],
    'data' : [
        'views/stock_move_view.xml'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
