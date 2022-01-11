# -*- coding: utf-8 -*-

from odoo import api, models, fields, SUPERUSER_ID, _
from odoo.exceptions import UserError

class InheritedPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    po_note = fields.Char(string='PO Note')


    def _prepare_picking(self):
        whout_vals = super(InheritedPurchaseOrder, self)._prepare_picking()
        whout_vals.update({
            'so_po_note': self.po_note,
        })
        return whout_vals

    # def button_confirm(self):
    #     for order in self:
    #         # print("################1#############",order)
    #         if order.state not in ['draft', 'sent']:
    #             # print("###############2##############")
    #             continue
    #         aaa = order._add_supplier_to_product()
    #         # print("###############3##############",aaa)


    #         # Deal with double validation process
    #         if order._approval_allowed():
    #             hh=order.button_approve()
    #             # print("###############4##############",hh)

    #         else:
    #             kk=order.write({'state': 'to approve'})
    #             # print("###############5##############",kk)

    #         if order.partner_id not in order.message_partner_ids:
    #             dd=order.message_subscribe([order.partner_id.id])
    #             # print("###############6##############",dd)
    #     picking = self.env['stock.picking'].search([('origin', '=', self.name)])
    #     if picking:
    #         picking.so_po_note = self.po_note
    #     picking_line=self.env['purchase.order.line'].
    #     stock_move=self.env['stock.move'].search([('move_ids_without_package', '=', )])

    #     return True


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    po_note_line = fields.Char(string='PO Note Line')

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        whout_vals = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        whout_vals.update({
            'so_po_note_line': self.po_note_line,
        })
        return whout_vals



    