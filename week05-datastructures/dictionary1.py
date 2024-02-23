# student.py
# a program that stores a student name and a list of her courses and grades in a dict, the program then prints out the data
# Author: Paul O'Shaughnessy


student = {
          'name' : 'Mary',
          'modules' : [{'coursename' : 'Programming', 'grade' : 45},
                        {'coursename' : 'History', 'grade' : 99}]
}

print('student: {}'.format(student['name']))
for module in student['modules']:
    print('\t {} \t {}'.format(module['coursename'], module['grade']))

