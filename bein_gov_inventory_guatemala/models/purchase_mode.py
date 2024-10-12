from odoo import fields, models

class PurchaseMode(models.Model):
    _name = 'bein_gov_inventory_guatemala.purchase_mode'
    _description = 'Purchase Mode'

    code = fields.Char(string="Código", required=True)
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
