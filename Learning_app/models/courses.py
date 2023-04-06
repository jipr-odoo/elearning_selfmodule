from odoo import fields,models,api
from odoo.exceptions import UserError

class courses(models.Model):
    _name ='courses'
    _description ='courses description'
    
    name = fields.Char()
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
        ], compute="_countfeedback",default='no'
    )
    course_students=fields.Many2many('student')

    @api.depends('test_available')
    def _test_no(self):
        for record in self:
            record.courses_test=len(record.test_available)


    @api.depends('course_students')
    def _countfeedback(self):
        for i in self:
            print('*********',i.id)
            c_Exc=0
            c_Avg=0
            c_good=0
            c_poor=0

            for record in self.course_students:
                print("========",record.course_type)

                for rec in record.course_type:
                    print("-------------",rec.id)

                    if i.id == rec.id:
                        print("?????????????",record.priority)
                        if record.priority == 'poor':
                            c_poor+=1
                        elif record.priority == 'good':
                            c_good+=1
                        elif record.priority == 'avg':
                            c_Avg+=1
                        elif record.priority == 'exc':
                            c_Exc+=1


            if(c_Exc>=c_Avg and c_Exc>=c_good and c_Exc>=c_poor):
                self.course_feedback='exc'

            elif(c_Avg>=c_Exc and c_Avg>=c_good and c_Avg>=c_poor):
                self.course_feedback='avg'

            elif(c_good>=c_Exc and c_good>=c_Avg and c_good>=c_poor):
                self.course_feedback='good'

            else:
                self.course_feedback='poor' 


        

        # self.course_feedback='good'
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
                








