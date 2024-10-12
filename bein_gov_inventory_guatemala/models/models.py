# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bein_gov_inventory_guatemala(models.Model):
#     _name = 'bein_gov_inventory_guatemala.bein_gov_inventory_guatemala'
#     _description = 'bein_gov_inventory_guatemala.bein_gov_inventory_guatemala'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

