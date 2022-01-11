# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    so_po_note = fields.Char(string='SO/PO Note')



class StockMove(models.Model):
    _inherit = 'stock.move'

    so_po_note_line = fields.Char(string='SO/PO Note')