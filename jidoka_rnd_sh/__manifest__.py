# -*- coding: utf-8 -*-
{
    'name': "RND Custom Jidoka SH",

    'summary': """
        RND Custom Jidoka SH Module create by Syarif Hidayatullah """,

    'description': """
        -
    """,

    'author': "Syarif Hidayatullah",
    'website': "-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale', 'jidoka_sale', 'design_process', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
