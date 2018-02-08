# -*- coding: utf-8 -*-

{
    'name' : 'Stock Back Date Valuation ',
    'version' : '1.1',
    'category': 'Hidden',
    'author': 'FlexERP',
    'website': 'www.flexerp.dk',
    'description': """
Menu Path: Inventory/Reporting/Inventory.
For Delivery Validating / Incoming receipts:
We can open Date of transfer / Date done on stock.picking and store this Date done on Stock.move with new field called "Back Date". So "Back Date" on stock move will be compute from Date done of picking/transfer.. And at end we may need to adapt this report Inventory/Reporting/Inventory which should consider backdate on stock move.
Currently date is taken from stock move - 
Schedule date and report is generated based on that
If we can create new field on stock move which is computed using 
date of transfer of related picking and use this new date field instead of stock move - schedule date then it can fix issue.
            """,
    'summary' : 'Stock Back Date Valuation ',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'depends' : ['stock_account'],
    'data' : [
            'views/stock_move_view.xml',
              ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
