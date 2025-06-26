from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    employee_id = fields.Many2one(
        'hr.employee', 
        string='Empleado', 
        help='Empleado que cargó este producto'
    )
