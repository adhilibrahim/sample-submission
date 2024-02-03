from odoo import models, fields, api


class InvoiceWarning(models.TransientModel):
    _name = 'invoice.warning'
    _description = 'Invoice Warning'

    sample_submission_id = fields.Many2one('sample.submission', string='Sample Submission', readonly=True)
    warning = fields.Text(string='Warning Message', readonly=True,
                          default="Are you sure you want to generate an invoice?")

    # To generate invoice
    def generate_invoice(self):
        invoice = self.env['account.move'].create({
            'partner_id': self.sample_submission_id.customer_id.id,
        })
        print("invoiceeeeeee", invoice)
        self.sample_submission_id.write({'invoiced': True})
        return {
            'type': 'ir.actions.act_window_close',
            'invoice': invoice.id
        }
