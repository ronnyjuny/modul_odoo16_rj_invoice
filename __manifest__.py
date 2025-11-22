{
    'name': 'Invoice Custom',
    'summary': 'Format invoice custom A5 & A4',
    'version': '1.0',
    'category': 'Accounting',
    'author': 'Ronny Lim',
    'website': 'https://instagram.com/rjtcl_soft',
    'depends': ['account'],
    'data': [
        'data/paperformat_data.xml',
        'report/report_invoice_mini.xml',
        'views/report_invoice_mini.xml',
        'views/invoice_form_button.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
