# -*- coding: utf-8 -*-
from odoo import models, fields

class Dependency(models.Model):
    _name = 'bein_gov_inventory_guatemala.dependency'
    _description = 'Dependencia'

    code = fields.Char(string="Código",required=True)
    name = fields.Char(string="Nombre",required=True)
    description =fields.Text(string="Descripción")
