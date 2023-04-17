from odoo import models,fields

class certificate(models.Model):
    _name ='course.certificate'
    _description='certificate description'

    name=fields.Char(required =True , string="Certificate Name")
    certi_logo=fields.Image()
    completed_course=fields.Many2one('courses',string="Course")
    grade=fields.Selection(
        selection=[
        ('a++','A++'),
        ('a','A'),
        ('b++','B++'),
        ('b','B'),
        ('c++','C++'),
        ('c','C'),
        ]
    )
    student_name=fields.Char()
    completion_date=fields.Date()



class applied_jobs(models.Model):
    _name='applied.jobs'
    _description='applied jobs description'   


