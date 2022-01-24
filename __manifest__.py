{
    'name': 'PO SO note',
    'version': '1.0',
    'sequence': 1,
    'summary': 'PO SO Note',
    'description': 'PO SO Note',
    'depends': ['base','sale','purchase','stock', 'purchase_stock'],
    'data': [
        'views/purchase_order_viewt.xml',
        'views/stock_picking_view.xml',
        'views/sale_order_view.xml',
        
        'report/sale_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
