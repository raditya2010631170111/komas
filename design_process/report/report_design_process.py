from odoo import models, _


class ReportDesignProcessXLSX(models.AbstractModel):
    _name = 'report.design_process.report_design_process_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):
        for obj in objects:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name)
            bold_header = workbook.add_format({'bold':True,'align':'center','valign':'vcenter'})
            bold_border_header = workbook.add_format({'border':1,'bold':True,'align':'center','valign':'vcenter'})
            bold_border_header.set_border_color('#000000')
            header = workbook.add_format({'align':'center','valign':'vcenter'})
            table_header = workbook.add_format({'border':1,'align':'center','valign':'vcenter'})
            body = workbook.add_format({'border':1,'align':'center','valign':'vcenter'})
            body_min = workbook.add_format({'align':'center','valign':'vcenter'})
            date_format = workbook.add_format({'num_format':'dd-MMM-yyyy'})
            border_right = workbook.add_format()
            border_right.set_right()
            ttd_format = workbook.add_format({'bold': True,'underline':True,'italic':True})
            ttd_format_center = workbook.add_format({'bold': True,'underline':True,'italic':True,'align':'center'})
            sheet.set_column(2, 2, 1)
            sheet.set_column(7, 7, 1)
            sheet.set_column(1, 1, 9)
            sheet.set_column(6, 6, 10)
            sheet.set_column(8, 8, 12)
            sheet.write('J8','',border_right)
            sheet.write('J9','',border_right)
            sheet.write('J10','',border_right)
            sheet.write('J11','',border_right)
            sheet.write('J12','',border_right)
            sheet.merge_range('A1:J1', obj.env.company.name, bold_header)
            sheet.merge_range('A3:J3', _('%s - %s')%( obj.env.company.street, obj.env.company.zip), header)
            sheet.merge_range('A4:J4', _('%s - %s') %(obj.env.company.state_id.name,obj.env.company.country_id.name), header)
            # sheet.merge_range('A5:J5', _('TEL : %s FAX : %s')%(obj.env.company.phone,obj.env.company.vat), header)
            sheet.merge_range('A5:J5', _('TEL : %s FAX : %s')%(obj.env.company.phone,obj.env.company.fax), header)
            sheet.write('I6','Page: 1  Of:1')
            sheet.merge_range('A7:J7', 'SAMPLE REQUEST', bold_border_header)
            sheet.write('A9','Buyer Requested No')
            sheet.write('C9',':',body_min)
            sheet.write('D9',obj.request_no,date_format)
            sheet.write('G9','Date Issued')
            sheet.write('H9',':',body_min)
            sheet.write('I9',obj.schedule_date,date_format)
            sheet.write('A10','Company')
            sheet.write('C10',':',body_min)
            sheet.write('D10',obj.partner_id.name)
            sheet.write('G10','Deadline')
            sheet.write('H10',':',body_min)
            sheet.write('I10',obj.deadline,date_format)
            sheet.write('A11','Purpose')
            sheet.write('C11',':',body_min)
            sheet.write('D11',obj.name)
            sheet.write('A13','Item No.',table_header)
            sheet.merge_range('B13:F13','Description',table_header)
            sheet.merge_range('G13:H13','Qty',table_header)
            sheet.merge_range('I13:J13','Remark',table_header)
            sheet.merge_range(14,0,15,0,'',table_header)
            sheet.merge_range(14,1,15,5,'MATERIAL : ',table_header)
            sheet.merge_range(14,6,15,7,'',table_header)
            sheet.merge_range(14,8,15,9,'',table_header)
            sheet.merge_range(18,0,18,1,'R&D MANAGER',ttd_format)
            sheet.merge_range(18,2,18,3,'R&D DEPT.',ttd_format)
            sheet.merge_range(18,4,18,6,'MARKETING MANAGER',ttd_format_center)
            sheet.merge_range(18,7,18,9,'MARKETING DEPT.',ttd_format_center)
            