# -*- coding: utf-8 -*-
{
    'name': 'Actualizar Costo en Factura de Compra',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Actualiza el costo del producto al confirmar facturas de compra',
    'description': """
        Actualización Automática de Costos de Productos
        ================================================
        
        Este módulo actualiza automáticamente el costo (standard_price) de los productos
        cuando se confirma una factura de compra (Vendor Bill).
        
        Características:
        ----------------
        * Actualiza el costo directamente con el precio de compra
        * Considera descuentos aplicados en las líneas
        * Solo afecta productos de tipo 'almacenable' (storable)
        * Se ejecuta automáticamente al confirmar la factura
        
        Uso:
        ----
        Una vez instalado, el módulo funciona automáticamente:
        1. Crea o selecciona una factura de proveedor
        2. Agrega productos y precios
        3. Al confirmar la factura, los costos se actualizan automáticamente
    """,
    'author': 'Trixocom',
    'website': 'https://github.com/trixocom',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'product',
        'purchase',
    ],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}