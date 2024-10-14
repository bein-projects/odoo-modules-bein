from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    dependency_id = fields.Many2one('bein_gov_inventory_guatemala.dependency',  string="Dependencia")
    purchase_mode_id = fields.Many2one('bein_gov_inventory_guatemala.purchase_mode',  string="Modalidad de compra")