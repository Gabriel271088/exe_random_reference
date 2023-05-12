# -*- coding: utf-8 -*-
import random
from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def reference_create(self):
        prefix = ''
        prefix = self.categ_id.ref_categ
        self.default_code = prefix + str(self.env['ir.sequence'].next_by_code('dis.analytic')) or '/'


class ProductCategory(models.Model):
    _inherit = 'product.category'

    ref_categ = fields.Char("Referencia Categoria")