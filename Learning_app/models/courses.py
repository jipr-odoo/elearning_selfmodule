from odoo import fields,models,api

class courses(models.Model):
    _name ='courses'
    _description ='courses description'

    name = fields.Char(required = True)
    user_id = fields.Text(required = True)
    mobile_no = fields.Integer()
    course_duration=fields.Selection(
        selection=[
        ('1','One Month'),
        ('3','Three Month'),
        ('6', 'Six Month'),
        ('7','One Year'),
        ('8','UnLimited')
        ]
    )
    course_ids = fields.Many2many('res_user')



class practice_test(models.Model):
    _name ='practice.test'
    _description='practice.test description'


    test_id=fields.Many2one('courses',string="Subject of test")
    








