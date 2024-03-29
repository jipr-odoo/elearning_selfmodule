from odoo import fields,models,api
from odoo.exceptions import UserError

class courses(models.Model):
    _name ='courses'
    _description ='courses description'
    
    name = fields.Char()
    description = fields.Html()
    course_duration = fields.Selection(
        selection=[
        ('1','One Week'),
        ('3','Three Month'),
        ('6', 'Six Month'),
        ('1y','One Year'),
        ('un','UnLimited')
        ]
    )
    course_fees=fields.Float(required=True)
    course_instructors=fields.Many2many('res.partner',string="Instructor")
    course_type=fields.Selection(
        selection=[
        ('tech','Technical'),
        ('nontech','Non Technical'),
        ('manage','Management'),
        ('law','Law of India')
        ]
    )
    test_availables=fields.One2many('survey.survey','sel_course',readonly=True)
    courses_test=fields.Integer(compute="_test_no",string ="No of Test Available")
    color=fields.Integer()
    course_feedback=fields.Selection(
        selection=[
        ('no','No Feedback'),
        ('poor','Poor'),
        ('good','Good'),
        ('avg','Average'),
        ('exc','Excellent')
        ], compute="_countfeedback",default='no'
    )
    course_students=fields.Many2many('student')
    student_count=fields.Integer(compute="_countStudent")

    @api.depends('course_students')
    def _countStudent(self):
        for record in self:
            self.student_count=len(record.course_students)


    @api.depends('test_availables')
    def _test_no(self):
        for record in self:
            record.courses_test=len(record.test_availables)


    @api.depends('course_students')
    def _countfeedback(self):
        for i in self:
            # print('*********',i.id)
            c_Exc=0
            c_Avg=0
            c_good=0
            c_poor=0

            for record in self.course_students:
                # print("========",record.course_type)

                for rec in record.course_type:
                    # print("-------------",rec.id)

                    if i.id == rec.id:
                        # print("?????????????",record.priority)
                        if record.priority == 'poor':
                            c_poor+=1
                        elif record.priority == 'good':
                            c_good+=1
                        elif record.priority == 'avg':
                            c_Avg+=1
                        elif record.priority == 'exc':
                            c_Exc+=1


            # print("@@@@@@@@@",c_Exc,c_Avg,c_good,c_poor)

            if(c_Exc>=c_Avg and c_Exc>=c_good and c_Exc>=c_poor):
                i.course_feedback='exc'

            elif(c_Avg>=c_Exc and c_Avg>=c_good and c_Avg>=c_poor):
                i.course_feedback='avg'

            elif(c_good>=c_Exc and c_good>=c_Avg and c_good>=c_poor):
                i.course_feedback='good'

            else:
                i.course_feedback='poor' 


    






