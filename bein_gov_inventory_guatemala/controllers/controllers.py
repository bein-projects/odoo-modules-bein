# -*- coding: utf-8 -*-
# from odoo import http


# class BeinGovInventoryGuatemala(http.Controller):
#     @http.route('/bein_gov_inventory_guatemala/bein_gov_inventory_guatemala', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bein_gov_inventory_guatemala/bein_gov_inventory_guatemala/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bein_gov_inventory_guatemala.listing', {
#             'root': '/bein_gov_inventory_guatemala/bein_gov_inventory_guatemala',
#             'objects': http.request.env['bein_gov_inventory_guatemala.bein_gov_inventory_guatemala'].search([]),
#         })

#     @http.route('/bein_gov_inventory_guatemala/bein_gov_inventory_guatemala/objects/<model("bein_gov_inventory_guatemala.bein_gov_inventory_guatemala"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bein_gov_inventory_guatemala.object', {
#             'object': obj
#         })

