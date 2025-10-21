# Actualización de Costos en Facturas de Compra - Odoo 18 CE

## Descripción

Módulo para Odoo 18 Community Edition que actualiza automáticamente el costo de los productos cuando se confirma una factura de compra.

## Características

✅ **Actualización Automática**: El costo se actualiza al confirmar la factura de compra  
✅ **Considera Descuentos**: Toma en cuenta los descuentos aplicados en las líneas  
✅ **Solo Productos Almacenables**: Afecta únicamente productos de tipo `product` (storable)  
✅ **Registro de Cambios**: Guarda log de cada actualización de costo  
✅ **Actualización Directa**: Reemplaza el costo anterior con el nuevo precio de compra  

## Instalación

### Opción 1: Instalación Manual

1. Clonar el repositorio:
```bash
git clone https://github.com/trixocom/odoo_purchase_cost_update.git
```

2. Copiar la carpeta a tu directorio de addons de Odoo:
```bash
cp -r odoo_purchase_cost_update /ruta/a/tu/odoo/addons/
```

3. Reiniciar el servicio de Odoo:
```bash
sudo systemctl restart odoo
# o
sudo service odoo restart
```

4. Actualizar la lista de aplicaciones:
   - Ir a **Aplicaciones**
   - Activar el **Modo Desarrollador**
   - Hacer clic en **Actualizar lista de aplicaciones**

5. Buscar e instalar:
   - Buscar "Actualizar Costo en Factura de Compra"
   - Hacer clic en **Instalar**

### Opción 2: Con Docker

```bash
# En tu docker-compose.yml, agregar el volumen:
volumes:
  - ./addons/odoo_purchase_cost_update:/mnt/extra-addons/odoo_purchase_cost_update

# O clonar directamente en el directorio de addons
cd /ruta/a/tus/addons
git clone https://github.com/trixocom/odoo_purchase_cost_update.git
```

### Opción 3: Con Git Installer (Recomendado)

Si tienes instalado el módulo `odoo_git_installer`:

1. Ir a **Configuración → Técnico → Git Installer**
2. Crear nuevo registro:
   - **Repository URL**: `https://github.com/trixocom/odoo_purchase_cost_update.git`
   - **Branch**: `main`
3. Hacer clic en **Install**

## Uso

Una vez instalado, el módulo funciona automáticamente:

1. **Crear Factura de Proveedor**:
   - Ir a **Contabilidad → Proveedores → Facturas**
   - Crear nueva factura

2. **Agregar Productos**:
   - Agregar líneas con productos
   - Especificar precios unitarios
   - Aplicar descuentos si es necesario

3. **Confirmar Factura**:
   - Al hacer clic en **Confirmar**
   - El costo de cada producto se actualiza automáticamente

## Ejemplo

**Antes de confirmar la factura:**
- Producto: Laptop HP
- Costo actual: $800.00
- Precio en factura: $850.00
- Descuento: 10%

**Después de confirmar:**
- Nuevo costo: $765.00 ($850 - 10% = $765)

## Verificación

Para verificar que el costo se actualizó:

1. Ir al producto: **Inventario → Productos → Productos**
2. Abrir el producto
3. Verificar el campo **Costo** en la pestaña de información general

## Logs

El módulo registra cada actualización en los logs de Odoo:

```bash
tail -f /var/log/odoo/odoo.log | grep "Costo actualizado"
```

## Compatibilidad

- ✅ Odoo 18.0 Community Edition
- ✅ Odoo 18.0 Enterprise Edition

## Dependencias

- `account` - Módulo de contabilidad
- `product` - Módulo de productos
- `purchase` - Módulo de compras

## Notas Técnicas

### Campo Actualizado

El módulo actualiza el campo `standard_price` del modelo `product.product`.

### Métodos Modificados

- `account.move.action_post()` - Intercepta la confirmación de facturas
- `account.move._update_product_cost()` - Método personalizado para actualizar costos

### Permisos

El módulo usa `sudo()` para asegurar que tenga permisos de escritura en el campo de costo.

## Personalización

Si deseas usar **costo promedio ponderado** en lugar de actualización directa, puedes modificar el método `_update_product_cost()` en `models/account_move.py`.

## Soporte

Para reportar problemas o sugerencias:

- 🐛 **Issues**: [GitHub Issues](https://github.com/trixocom/odoo_purchase_cost_update/issues)
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/trixocom/odoo_purchase_cost_update/discussions)

## Licencia

LGPL-3

## Autor

**Trixocom**  
GitHub: [@trixocom](https://github.com/trixocom)

## Changelog

### Version 18.0.1.0.0
- ✨ Versión inicial
- ✅ Actualización directa de costos al confirmar facturas
- ✅ Soporte para descuentos
- ✅ Logging de cambios

---

⭐ Si te gusta este módulo, no olvides darle una estrella en GitHub!