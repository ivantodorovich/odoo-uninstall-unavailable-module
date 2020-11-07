from odoo import api, fields, models


class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
