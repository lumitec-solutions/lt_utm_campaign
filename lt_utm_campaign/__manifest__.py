##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
{
    'name': "Marketing/UTM Campaign",
    'summary': "customizations related to Marketing/UTM Campaign",
    'author': "lumitec GmbH",
    'website': "https://www.lumitec.solutions",
    'category': 'Extra Tools',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'images': ['static/description/thumbnail.gif'],
    'depends': [
        'base',
        'utm',
        'project',
        'calendar',
        'event',
        'website',
        'link_tracker',
        'mass_mailing',
        'marketing_automation',
        'website_sale',
    ],
    'data': [
        'views/project_views.xml',
        'views/calendar_event_views.xml',
        'views/event_views.xml',
        'views/utm_campaign_views.xml',
        'views/website_visitor_views.xml'
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
