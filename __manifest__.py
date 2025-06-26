{
    'name': 'Sale Order Employee',
    'version': '18.0',
    'category': 'Sales',
    'summary': 'Permite seleccionar al empleado en la línea de pedido de ventas',
    'depends': ['sale_management', 'hr'],
    'data': [
        'views/sale_order_line_views.xml',
        'views/sale_order_form_inherit_employee.xml',
        ],
    'installable': True,
    'application': False,
}
