# -*- coding: utf-8 -*-

from odoo import api, models, fields, SUPERUSER_ID, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_note = fields.Char(string='SO Note')
    discount_by = fields.Selection([('percentage','Percentage'),
                                    ('amount','Amount')],
                                    string="Discount By")

    discount_amount = fields.Float(string="Discount Amount")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    so_note_line = fields.Char(string='SO Note')

    def _prepare_procurement_values(self, group_id=False):
       
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({
            'so_po_note_line': self.so_note_line,
        })
        return values
