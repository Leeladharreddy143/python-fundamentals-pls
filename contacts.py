contacts = {
    'number': 4,
    'students':[
                {'name':'Leela', 'email':'leela@exmp.com'},
                {'name':'Leeladhar', 'email':'Leeladhar@exmp.com'},
                {'name':'Sarah', 'email':'sarah@exmp.com'},
                {'name':'uday', 'email':'uday@exmp.com'}
                
                ]
}


for student in contacts['students']:
    print(student['email'])