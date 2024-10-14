# -*- coding: utf-8 -*-
{
    'name': "Inventario (Gobierno Guatemala)",

    'summary': "Manejo ingresos y salidas de inventario conforme a la legislación de Guatemala",

    'description': """
Inventario Gobierno Guatemala
    """,

    'author': "Bein technologies",
    'website': "https://beintechnologies.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bein_menus.xml',
        'views/bein_dependency_views.xml',
        'views/bein_purchase_mode_views.xml',
        'views/purchase_order_views.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

