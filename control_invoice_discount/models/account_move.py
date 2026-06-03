from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        max_discount_param = self.env['ir.config_parameter'].sudo().get_param('control_invoice_discount.max_invoice_discount', default=0.0)
        max_allowed_discount = float(max_discount_param)
        
        if max_allowed_discount > 0:
            for move in self:
                if move.move_type == 'out_invoice':
                    for line in move.invoice_line_ids:
                        if line.display_type != 'product':
                            continue
                        
                        if line.discount > max_allowed_discount:
                            raise ValidationError(_(f"Validare refuzată! Pe linia cu produsul '{line.product_id.name}' ați aplicat un discount de {line.discount:.2f}%, "
                                f"Discount maxim permis {max_allowed_discount:.2f}%."))
        return super(AccountMove, self).action_post()