from odoo import api, fields, models, _


class MaterialRequirementWizard(models.TransientModel):
    _name = 'material.requirement.wizard'
    _description = 'Material Requirement Wizard'

    sl_no = fields.Integer(string='Sl No.')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    remarks = fields.Text(string='Remarks')

    # Function for creating records in one2many field named material_line_ids
    def create_records(self):
        values = [
            {'sl_no': self.sl_no, 'product_id': self.product_id.id, 'quantity': self.quantity, 'remarks': self.remarks},
        ]
        self.env['sample.submission'].browse(self._context.get('active_id')).write({
            'material_line_ids': [(0, 0, val) for val in values]
        })
        return {'type': 'ir.actions.act_window_close'}
