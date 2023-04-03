from odoo import fields,models,api

class ratings(models.Model):
    _name="ratings.tag"
    _description="ratings ka description"

    name=fields.Char(required=True)
    color=fields.Integer()
