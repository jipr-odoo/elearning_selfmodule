from odoo import fields,models,api

class practice_test(models.Model):
    _name ='practice.test'
    _description='practice.test description'
    

    
    name=fields.Char()
    sel_course=fields.Many2one('courses',string="Select course")
   
