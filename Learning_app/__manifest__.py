{
    'name': "Learning_app",
    'version': '0.1.0',
    'depends': ['base'],
    'author': "jipr",
    'category': 'education management',
    'description': """Description text""",
    'data': [
        'security/ir.model.access.csv',
        'views/courses_views.xml',
        'views/jobs_views.xml',
        'views/reports_views.xml',
        'views/courses_menus.xml'  
    ],
    'demo': [
        
    ],
    'installable' : True,
    'application' : True,
    'auto_install': True,
    'license': 'LGPL-3',
}
