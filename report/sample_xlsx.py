from odoo import api, fields, models, _


class SampleSubmissionXlsx(models.AbstractModel):
    _name = 'report.sample_submission.report_sample_sub_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Sample Excel')
        title_format = workbook.add_format({'bold': True, 'font_size': 12, 'underline': True})
        sheet.write(0, 0, 'Sample Submission Report', title_format)
        bold_and_clr = workbook.add_format({'bold': True, 'color': 'red'})
        sheet.set_column('A:A', 16)
        sheet.set_column('B:B', 12)
        row = 1
        col = 1
        for obj in partners:
            sheet.write(row, col - 1, 'Customer Name', bold_and_clr)
            sheet.write(row, col, obj.customer_id.name)
            row += 1

            sheet.write(row, col - 1, 'Reference', bold_and_clr)
            sheet.write(row, col, obj.reference)
            row += 1

            sheet.write(row, col - 1, 'Date of Submission', bold_and_clr)
            sheet.write(row, col, obj.submission_date)
            row += 1

            sheet.write(row, col - 1, 'Description', bold_and_clr)
            sheet.write(row, col, obj.note)
            row += 1

            sheet.write(row, col - 1, 'Price', bold_and_clr)
            sheet.write(row, col, obj.price)
            row += 1

            sheet.write(row, col - 1, 'Discount', bold_and_clr)
            sheet.write(row, col, obj.discount)
            row += 1

            sheet.write(row, col - 1, 'VAT', bold_and_clr)
            sheet.write(row, col, obj.vat)
            row += 1

            sheet.write(row, col - 1, 'Stage', bold_and_clr)
            sheet.write(row, col, obj.stages)
            row += 1

            row += 2
