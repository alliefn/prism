# -*- coding: utf-8 -*-
{
    'name': "Prism",
    'summary': 'Sistem informasi untuk mengelola volunteer Chempro dalam verifikasi jawaban soal',
    'description': 'Sistem informasi untuk mengelola volunteer Chempro dalam verifikasi jawaban soal',
    'sequence': -100,
    'author': "Tim CintaSI",
    'category': 'Human Resources',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cats_menus.xml',
        'views/cats_trees.xml',
        'views/cats_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
