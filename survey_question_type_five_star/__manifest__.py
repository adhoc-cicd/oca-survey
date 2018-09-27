# -*- coding: utf-8 -*-
# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Survey five stars question type',
    'summary': """
        This module add five stars rating as question type for survey page""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/survey',
    'depends': [
        'survey'
    ],
    'data': [
        'views/survey_question.xml',
        'views/survey_template.xml',
    ],
    'demo': [
    ],
}
