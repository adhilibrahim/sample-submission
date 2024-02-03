from odoo import api, fields, models, _


class SampleSubmission(models.Model):
    _name = "sample.submission"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    _description = "Sample Submission"

    customer_id = fields.Many2one('res.partner', string="Customer Name", tracking=True)
    image = fields.Binary(string="Customer Image", tracking=True)
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    submission_date = fields.Date(string="Date of Submission", required=True, tracking=True)
    note = fields.Text(string='Description', tracking=True)
    price = fields.Float(string='Price', tracking=True)
    discount = fields.Float(string='Discount', tracking=True)
    vat = fields.Float(string='VAT', tracking=True)
    stages = fields.Selection(
        [('pending', 'Pending'), ('doing', 'Doing'), ('completed', 'Completed')],
        string='Stage', default='doing', tracking=True)
    material_line_ids = fields.One2many('materials.line', 'material_id', string='Materials')
    invoiced = fields.Boolean(string='Invoiced', default=False, readonly=True)

    def action_pending(self):
        for rec in self:
            rec.stages = 'pending'

    def action_doing(self):
        for rec in self:
            rec.stages = 'doing'

    def action_completed(self):
        for rec in self:
            rec.stages = 'completed'

    # Sequence generation
    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('sample.sample') or _('New')
        res = super(SampleSubmission, self).create(vals)
        return res

    # to show waring message from wizard
    def confirm_invoice(self):
        return {
            'name': _('Generate Invoice Warning'),
            'type': 'ir.actions.act_window',
            'res_model': 'invoice.warning',
            'view_mode': 'form',
            'view_id': self.env.ref('sample_submission.view_generate_invoice_warning').id,
            'target': 'new',
            'context': {'default_sample_submission_id': self.id},
        }


# model for one2many field
class MaterialsLine(models.Model):
    _name = 'materials.line'
    _description = 'Materials Required'

    sl_no = fields.Integer(string='Sl No.')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    remarks = fields.Text(string='Remarks')
    material_id = fields.Many2one('sample.submission', string='Materials')
