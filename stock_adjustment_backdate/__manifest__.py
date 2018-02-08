# -*- coding: utf-8 -*-
{
    'name' : 'Stock Adjustment Backdate',
    'version' : '1.1',
    'category': 'Warehouse',
    'license': 'Other proprietary',
    'author': 'FlexERP',
    'website': 'www.flexerp.dk',
    'price': 0.0,
    'currency': 'EUR',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'summary': 'Stock Adjustment Backdate',
    'description' : '''
    ​1. Stock Valuation Report to include backdated Inventory Adjustment. At present, we change the Inventory Date during inventory adjustment process but the confirm date is still today's date (date_done or date of operation).​

could not understand fully what exactly issue. I have seen that Inventory date on inventory adjustment is readonly mode then how did you change that ?

The read only will be changed to readonly="0" so that it is changeable, eg: if I made an inventory adjustment and changed the date to 1 May 2017, when validated the date should be 1 May 2017 not today's date (which it is currently is). And when we go to inventory at date, and select 1 May 2017, the inventory adjustment should be displayed in there not for today's date.
​
For inventory adjustment: 
Currently if you see Date on inventory adjustment is locked so we can open it and allow user to enter any date on that date field and pass this date to stock move. That means we have to add new field on stock move called "Date Adjusment" and this date will be filled from inventory adjusment when you validate that adjusment.... And important thing is when stock move is going to done we can change of stock move original date field on odoo with "Date Adjusment"...


''',
    'depends' : ['stock'],
    'data' : [
              'views/stock_inventory_view.xml'
              ],
    'installable' : True,
    'auto_install' : False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
