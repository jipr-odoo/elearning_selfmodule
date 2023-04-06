from odoo import fields,models,api
from odoo.exceptions import UserError

class student(models.Model):
    _name='student'
    _description="student description"
    

    name =fields.Char(required=True)
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
    
    practice_test_no=fields.Integer(compute="_ctest_no", store=True)

    @api.depends('course_type')
    def _ctest_no(self):
        # # for record in self.course_type:
        #     # print("------------", self.course_type.mapped('courses_test'))
        # print("----------------------", self)
        for record in self.course_type:
            self.practice_test_no+=record.courses_test
    

    # @api.constrains('course_type')
    # def _countfeedback(self):
    #     # for i in self:
    #     #     print('*********',i.id)
    #     for record in self.course_type:
    #         print("{{{{{{{{{{{}}}}}}}}}}}",record)

    #     for record in self.course_type:
    #         print("====***********====",record.id)

    #             # if self.course_type == record.id:
    #             #     print("------found---------")
    #             # for rec in record.course_type:
    #             #     print("-------------",rec.id)
    #             #     if i.id == rec.id:
    #             #         print("!!!!!!!!!!!")
                
        
    
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
        ('unique_userId','unique(name)',
         'The userId should be unique')
    ] 


