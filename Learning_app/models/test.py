from odoo import fields,models,api

class practice_test(models.Model):
    _name="survey.survey"
    _description='practice.test description'
    _inherit="survey.survey"

    
    name=fields.Char(required =True)
    sel_course=fields.Many2one('courses',string="Select course")
    
    _sql_constraints = [
        ('unique_name','unique(name)',
         'The Test Name should be unique')
    ] 
