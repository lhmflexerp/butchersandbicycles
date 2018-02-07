# -*- coding: utf-8 -*-
{
    'name' : 'Stock Account Extend',
    'version' : '1.0',
    'category': 'Warehouse Management',
    'license': 'Other proprietary',
    'author': 'Alex Lyngsoe',
    'website': 'www.odoo.com',
    'summary': 'Stock Accounting',
    'description' : '''
    In Journal Entries, we would like to have the date of transfer in the date field just like the
    sales order and auto posted in the status 
''',
    'depends' : ['stock_account',
                 'stock_adjustment_backdate',
                 'stock_backdate_valuation'],
    'data' : [
        'views/stock_move_view.xml',
             ],
    'installable' : True,
    'auto_install' : False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
