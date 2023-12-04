{
    "name" : "Hospital",
    'version' : '16.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
School Management 
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends' : ['base',"contacts","sale"],
    'data': [
        'views/hospital_hospital_views.xml',
        'views/menu.xml',
        'views/hospital_department.xml',
        'security/ir.model.access.csv',
        'views/medicine.xml',
        'views/contact.xml',
        'views/sale.xml'

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
