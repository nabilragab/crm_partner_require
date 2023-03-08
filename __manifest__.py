# pylint: disable=missing-docstring, manifest-required-author
{
    'name': 'CRM Partner Require',
    'summary': 'Make partner required in opportunity',
    'author': 'CORE B.P.O',
    'maintainer': 'Abdalla Mohamed',
    'website': 'http://www.core-bpo.com',
    'version': '15.0.1.0.0',
    'category': 'Sales/CRM',
    'license': 'OPL-1',
    'depends': [
        'crm',
    ],
    'data': [
        'views/crm_lead.xml',
    ],
    'images': [
        'static/description/banner.gif',
        'static/description/main_screenshot.gif',
        'static/description/corebpo_logo.png',
        'static/description/opportunity_quick_create.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
