# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sample Submission',
    'version': '1.2',
    'summary': 'Submission of Samples Related App',
    'sequence': 10,
    'description': """ The goal of this project is to create a custom Odoo app called "sample-submission". This
     app aims to streamline the management of sample submissions, connect customers to
     submission forms, keep track of materials as products related to sample-submission,
     and generate invoices. Additionally, the app will support the generation of PDF and
     Excel reports with specific data and formatting requirements
    """,
    'category': 'Custom/Industry Solutions',
    'website': 'https://www.sample.com/app/solution',
    'images': [],
    'depends': ['mail', 'report_xlsx'],
    'license': 'LGPL-3',
    'data': [

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
