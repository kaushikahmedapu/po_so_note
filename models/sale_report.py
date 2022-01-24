from odoo import api, models

class SaleReport(models.AbstractModel):
    _name = 'report.po_so_note.sale_order_picking_all_operation_document'


    @api.model
    def _get_report_values(self, docids, data=None):
        print("$$$$$$$$$$$$docids$$$$$$$$$$$",docids)
        docs = self.env['stock.picking'].search([('sale_id','=',docids[0])])
        # docs_custom = self.env['stock.picking'].search([('id','=',docids[0])])
        # print(':::::::::::::using search:::::::::::',docs_custom)

        # aaa= self.env['stock.picking'].search([('sale_id','in',docids)])
        # print("##############docids11##############",aaa
       
        data = []
        print("#######################data#############",data)
        # for doc in docs:
        #     val = {
        #         'name': doc.name,
        #         'origin': doc.origin,
        #        }
        #     aaa=data.append(val)
        #     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",aaa)
        # print("$$$$$$$$$$$$$$3333$$$$$$$$$$",docs)
        return {
        'docs':docs,
        # 'data':self.data,
        # 'get_custom_report_report': self._get_data_from_report(data['form']),
        # 'res_id':self.stock_picking_id.id,
        }
    #     # print("$$$$$$$$$$$$$$$$$$$$$$$$",docs)

    #     # print("$$$$$$$$$$$$$$$$$$$$$$$$",docs)
    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     rslt = super()._get_report_values(docids, data)
    #     rslt['report_type'] = data.get('report_type') if data else ''
    #     return rslt
