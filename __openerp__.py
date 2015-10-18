# -*- coding: utf-8 -*-
{
    'name': "mediatek",

    'summary': "Personal media loan manager",

    'description': """
        Manages personal loans of medias.
        Just like a mediatek ;)
    """,

    'author': "Raphaël Doursenaud",
    'website': "http://raphael.doursenaud.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views.xml',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}