from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_fill_employees(self):
        for order in self:
            # Buscar la primera línea que tenga un empleado asignado
            first_employee = next(
                (line.employee_id for line in order.order_line if line.employee_id), 
                False
            )
            if first_employee:
                for line in order.order_line:
                    if not line.employee_id:
                        line.employee_id = first_employee
