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
    discount = fields.Float(string='Discount',compute ="_compute_discount_custom", store = True)

    @api.depends('discount_by', 'discount_amount')
    def _compute_discount_custom(self):
        for val in self:
            if val.discount_by == 'percentage':
                val.discount = (val.discount_amount * val.amount_untaxed)/100
                val.amount_total = val.amount_untaxed - val.discount
            if val.discount_by == 'amount':
                val.discount = val.discount_amount
                val.amount_total = val.amount_untaxed - val.discount


    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     docs = self.env['stock.picking'].browse(docids)
    #     data = []
    #     for doc in docs:
    #         val = {
    #             'name': doc.name,
    #             'origin': doc.origin,
    #            }
    #     data.append(val)

    #     return {
    #     'docs':docs,
    #     # 'data':data,
    #     }

        # print("#############################################",self.discount)


        # for m in self:
        #     journal_type = m.invoice_filter_type_domain or 'general'
        #     company_id = m.company_id.id or self.env.company.id
        #     domain = [('company_id', '=', company_id), ('type', '=', journal_type)]
        #     m.suitable_journal_ids = self.env['account.journal'].search(domain)

    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     docs = self.env['stock.picking'].browse(docids)
    #     data = []
    #     for doc in docs:
    #         val = {
    #             'name': doc.name.name,
    #             'origin': doc.origin,
    #             # 'payroll': doc.employee_id.payroll_no,
    #            }
    #     data.append(val)

    #     return {
    #     'docs':docs,
    #     'data': data,
    #     }


    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     report_obj = self.env['ir.actions.report']
    #     report = report_obj._get_report_from_name('module.report_name')
    #     docargs = {
    #         'doc_ids': docids,
    #         'doc_model': report.model,
    #         'docs': self,
    #     }
    #     return docargs

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    so_note_line = fields.Char(string='SO Note')
    # discount = fields.Float(string='Discount')

    def _prepare_procurement_values(self, group_id=False):
       
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({
            'so_po_note_line': self.so_note_line,
        })
        return values
