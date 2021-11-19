# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Prism - Chempro Skills Management',
    'category': 'Human Resources/Employees',
    'sequence': 270,
    'version': '1.0',
    'author': "Tim CintaSI",
    'summary': 'Manage skills, knowledge and resumé of your employees',
    'description':
        """
Achievements and Contributions for HR
========================

This module introduces achievement and contribution management for Chempro employees.
        """,
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_skills_security.xml',
        'views/hr_views.xml',
        'data/hr_resume_data.xml',
    ],
    'demo': [
        'data/hr_resume_demo.xml',
        'data/hr.employee.skill.csv',
        'data/hr.resume.line.csv',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'hr_skills/static/src/css/hr_skills.scss',
            'hr_skills/static/src/js/resume_widget.js',
        ],
        'web.qunit_suite_tests': [
            'hr_skills/static/tests/**/*',
        ],
        'web.assets_qweb': [
            'hr_skills/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
