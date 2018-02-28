# -*- coding: utf-8 -*-
{
    'name' : 'Sale Analysis Report Extend',
    'version' : '1.0',
    'category': 'Sales',
    'license': 'Other proprietary',
    'author': 'Alex Lyngsoe',
    'website': 'www.odoo.com',
    'summary': 'Sale Analysis Report Extend',
    'description' : '''
Add Custom fields in sale analysis report:
- Partner State
- Expected shipping date (Requested Date)
''',
    'depends' : ['sale_order_dates'],
    'data' : [
        'views/sale_view.xml'
    ],
    'installable' : True,
    'auto_install' : False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: