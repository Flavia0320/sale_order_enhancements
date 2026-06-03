from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    max_invoice_discount = fields.Float(
        string='Discount Maxim Permis (%)',
        config_parameter='control_invoice_discount.max_invoice_discount',
        help='Plafonul maxim de discount pe care un operator îl poate aplica pe o linie de factură.'
    )
