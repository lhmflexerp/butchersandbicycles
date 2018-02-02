# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Inventory(models.Model):
    _inherit = "stock.inventory"

    date = fields.Datetime(
        'Inventory Date',
        readonly=False, 
    )
    
    @api.multi
    def action_start(self):
        #Fully Overwrite this method to set Inventory Date
        for inventory in self:
            #vals = {'state': 'confirm', 'date': fields.Datetime.now()}
            vals = {'state': 'confirm', 'date': inventory.date}
            if (inventory.filter != 'partial') and not inventory.line_ids:
                vals.update({'line_ids': [(0, 0, line_values) for line_values in inventory._get_inventory_lines_values()]})
            inventory.write(vals)
        return True
    #prepare_inventory = action_start

class InventoryLine(models.Model):
    _inherit = "stock.inventory.line"
    
    
    def _get_move_values(self, qty, location_id, location_dest_id, out):
    #def _get_move_values(self, qty, location_id, location_dest_id):
        res = super(InventoryLine, self)._get_move_values(qty, location_id, location_dest_id, out)
        res.update({'date_adjustment':  self.inventory_id.date})
        return res
