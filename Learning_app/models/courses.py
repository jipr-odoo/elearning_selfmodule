from odoo import fields,models,api
from odoo.exceptions import UserError

class student(models.Model):
    _name='student'
    _description="student description"
    _rec_name="st_name"

    st_name =fields.Char(required=True)
    mobile_no = fields.Integer()
    id=fields.Integer(required =True, copy=False , string='UserId')
    course_type=fields.Many2many('courses', string='Course',required=True)
    state=fields.Selection(
        selection=[
        ('new','New'),
        ('enr','Enrolled'),
        ('paid','Paid'),
        ('ntpaid','Free')
        ],default='enr'
    )
    
    # practice_test_no=fields.Integer(related="course_type.c_test_no" ,stored=True)
    # feedback=fields.Many2one('ratings.tag',string="FeedBack for Course")
    
    priority=fields.Selection(
        selection=[
        ('no','No Feedback'),
        ('poor','Poor'),
        ('good','Good'),
        ('avg','Average'),
        ('exc','Excellent')
        ],string ="Feedback for Course"
    )
    
    practice_test_no=fields.Integer(compute="_ctest_no", stored=True)
    @api.depends('course_type')
    def _ctest_no(self):
            test = 0
            for record in self.course_type:
                print("--------------------", record.courses_test)
                test+=record.courses_test

    
    def paid(self):
        for record in self:
            if record.state!='paid':
                record.state='paid'
    

    def free(self):
        for record in self:
            print(len(record.course_type))
            if record.state!='ntpaid':
                record.state='ntpaid'
                


    _sql_constraints = [
        ('unique_userId','unique(st_name)',
         'The userId should be unique')
    ] 



class courses(models.Model):
    _name ='courses'
    _description ='courses description'
    _rec_name='course_name'

    course_name = fields.Char(required = True)
    course_duration=fields.Selection(
        selection=[
        ('1','One Month'),
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
    test_available=fields.One2many('practice.test','sel_course')
    courses_test=fields.Integer(compute="_test_no",string ="No of Test Available")
    color=fields.Integer()
    course_feedback=fields.Selection(
        selection=[
        ('no','No Feedback'),
        ('exc','Excellent'),
        ('avg','Average'),
        ('good','Good'),
        ('poor','Poor')
        ], compute="_countfeedback"
    )
    course_enrolled_testAvailable=fields.Many2many('student')

    @api.depends('test_available')
    def _test_no(self):
        for record in self:
            record.courses_test=len(record.test_available)


    @api.depends('course_enrolled_testAvailable')
    def _countfeedback(self):
        self.course_feedback='good'
        return
        
        # c_Exc=0
        # c_Avg=0
        # c_good=0
        # c_poor=0

        # f or record in self:
        #     if(record.c_st_enr.priority == 'poor'):
        #         c_poor+=1

        #     elif (record.c_st_enr.priority == 'good'):
        #         c_good+=1

        #     elif(record.c_st_enr.priority == 'avg'):
        #         c_Avg+=1

        #     else:
        #         c_Exc+=1
                    
         
        # if(c_Exc>=c_Avg and c_Exc>=c_good and c_Exc>=c_poor):
        #     self.course_feedback='exc'

        # elif(c_Avg>=c_Exc and c_Avg>=c_good and c_Avg>=c_poor):
        #     self.course_feedback='avg'

        # elif(c_good>=c_Exc and c_good>=c_Avg and c_good>=c_poor):
        #     self.course_feedback='good'

        # else:
        #     self.course_feedback='poor'
                














class practice_test(models.Model):
    _name ='practice.test'
    _description='practice.test description'
    

    
    test_names=fields.Char()
    sel_course=fields.Many2one('courses',string="Select course")
   








