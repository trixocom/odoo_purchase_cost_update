# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        """
        Sobrescribe el método action_post para actualizar el costo 
        de los productos cuando se confirma una factura de compra
        """
        res = super(AccountMove, self).action_post()
        
        for move in self:
            # Solo procesar facturas de compra (vendor bills)
            if move.move_type == 'in_invoice' and move.state == 'posted':
                move._update_product_cost()
        
        return res
    
    def _update_product_cost(self):
        """
        Actualiza el costo (standard_price) de cada producto 
        en las líneas de la factura
        """
        self.ensure_one()
        
        for line in self.invoice_line_ids:
            # Solo actualizar productos almacenables
            if line.product_id and line.product_id.type == 'product':
                # Obtener el precio unitario de la línea
                unit_price = line.price_unit
                
                # Considerar descuentos si existen
                if line.discount:
                    unit_price = unit_price * (1 - line.discount / 100.0)
                
                # Actualizar el costo del producto
                # Usamos sudo() para asegurar permisos de escritura
                line.product_id.sudo().write({
                    'standard_price': unit_price
                })
                
                _logger.info(
                    f"Costo actualizado para producto {line.product_id.name}: "
                    f"{unit_price:.2f} (Factura: {self.name})"
                )