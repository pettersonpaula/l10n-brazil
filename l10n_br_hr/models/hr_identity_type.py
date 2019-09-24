# (c) 2014 Kmee - Luis Felipe Mileo <mileo@kmee.com.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class HrIdentityType(models.Model):
    _name = 'hr.identity.type'

    name = fields.Char(
        string='Identity type')

    initials = fields.Char(
        string='Initials')

    employee_ids = fields.Many2many(
        string="Employees",
        comodel_name='hr.employee')
