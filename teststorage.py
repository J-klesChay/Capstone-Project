from storage import *

#Testing individual classes
student = Student('Gary', 17, 2022, 2023, '2227')
print(vars(student))
print(student)
print('')
c = Class('2227', 'J2')
print(c)
print('')
subject = Subject('H2MATH', 'H2')
print(subject)
print('')
studentsubject = StudentSubject('Gary', 'H2MATH')
print(studentsubject)
print('')
cca = CCA('robotics', 'club')
print(cca)
print('')
studentcca = StudentCCA('Gary', 'robotics', 'member')
print(studentcca)
print('')
activity = Activity('NOI', '17 Apr', '18 Apr')
print(activity)
print('')
studentactivity = StudentActivity('Gary', 'NOI', 'JC category', 'participant', 'bronze', '4')
print(studentactivity)
print('')

tuple = ('student_name', 'subject_name')
string = remove_quotes_in_tuple(tuple)
print(string)

#Testing StudentCollection Class
print('Testing StudentCollection Class')
s = StudentCollection()
print(s)
print('')

student1 = Student('Gary', 17, 2022, 2023, '2227')
record1 = vars(student1)
print(f'Inserting record {record1}')
s.insert(record1)
print(s)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
s.insert(record1)
print(s)
print('')

student2 = Student('Jkles', 17, 2022, 2023, '2227')
record2 = vars(student2)
print(f'Inserting record {record2}')
s.insert(record2)
print(s)
print('')

student1.class_ = '1234'
new_record1 = vars(student1)
print(f'Updating record {student1.name} to {new_record1}')
s.update('Gary', new_record1)
print(s.find('Gary'))
print(s)
print('')

print(f'Deleting record {student1.name}')
s.delete('Gary')
print(s)
print('')

print(f'Deleting record {student2.name}')
s.delete('Jkles')
print(s)
print('')

print(f'Finding record {student1.name}(Should return none)')
print(s.find('Gary'))
print('')

print(f'Deleting record {student1.name} again(Should give error)')
s.delete('Gary')
print('')


#Testing ClassCollection Class
print('Testing ClassCollection Class')
c = ClassCollection()
print(c)
print('')

class1 = Class('2227', 'JC2')
record1 = vars(class1)
print(f'Inserting record {record1}')
c.insert(record1)
print(c)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
c.insert(record1)
print(c)
print('')

class2 = Class('2314', 'JC1')
record2 = vars(class2)
print(f'Inserting record {record2}')
c.insert(record2)
print(c)
print('')

class1.level = 'JC3'
new_record1 = vars(class1)
print(f'Updating record {class1.name} to {new_record1}')
c.update('2227', new_record1)
print(c.find('2227'))
print(c)
print('')

print(f'Deleting record {class1.name}')
c.delete('2227')
print(c)
print('')

print(f'Deleting record {class2.name}')
c.delete('2314')
print(c)
print('')

print(f'Finding record {class1.name}(Should return none)')
print(c.find('2227'))
print('')

print(f'Deleting record {class1.name} again(Should give error)')
c.delete('2227')
print('')


#Testing SubjectCollection Class
print('Testing SubjectCollection Class')
c = SubjectCollection()
print(c)
print('')

subject1 = Subject('H2MATH', 'H2')
record1 = vars(subject1)
print(f'Inserting record {record1}')
c.insert(record1)
print(c)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
c.insert(record1)
print(c)
print('')

subject2 = Subject('H3COMPUTING', 'H3')
record2 = vars(subject2)
print(f'Inserting record {record2}')
c.insert(record2)
print(c)
print('')

subject1.level = 'H3'
new_record1 = vars(subject1)
print(f'Updating record {subject1.name} to {new_record1}')
c.update('H2MATH', new_record1)
print(c.find('H2MATH'))
print(c)
print('')

print(f'Deleting record {subject1.name}')
c.delete('H2MATH')
print(c)
print('')

print(f'Deleting record {subject2.name}')
c.delete('H3COMPUTING')
print(c)
print('')

print(f'Finding record {subject1.name}(Should return none)')
print(c.find('H2MATH'))
print('')

print(f'Deleting record {subject1.name} again(Should give error)')
c.delete('H2MATH')
print('')


#Testing StudentSubjectCollection Class
print('Testing StudentSubjectCollection Class')
s = StudentSubjectCollection()
print(s)
print('')

studentsubject1 = StudentSubject('Gary', 'H2COMPUTING')
record1 = vars(studentsubject1)
print(f'Inserting record {record1}')
s.insert(record1)
print(s)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
s.insert(record1)
print(s)
print('')

studentsubject2 = StudentSubject('Jkles', 'H2MATH')
record2 = vars(studentsubject2)
print(f'Inserting record {record2}')
s.insert(record2)
print(s)
print('')

#To show that primary key is composite(consisting of student_name and student_subject), hence there can be 2 entires with same name(Gary), but different subjects
studentsubject3 = StudentSubject('Gary', 'H2ECONS')
record3 = vars(studentsubject3)
print(f'Inserting record {record3}')
s.insert(record3)
print(s)
print('')

studentsubject1.subject_name = 'H2PHYSICS'
new_record1 = vars(studentsubject1)
print(f'Updating record ("Gary", "H2COMPUTING") to {new_record1}')
s.update(('Gary', 'H2COMPUTING'), new_record1)
print(s.find(('Gary', 'H2PHYSICS')))
print(s)
print('')

print(f'Deleting record ("Gary", "H2PHYSICS")')
s.delete(('Gary', 'H2PHYSICS'))
print(s)
print('')

print(f'Deleting record ("Jkles", "H2MATH")')
s.delete(('Jkles', 'H2MATH'))
print(s)
print('')

print(f'Finding record ("Gary", "H2PHYSICS")(Should return none)')
print(s.find(('Gary', 'H2PHYSICS')))
print('')

print(f'Deleting record ("Gary", "H2PHYSICS") again(Should give error)')
s.delete(('Gary', 'H2PHYSICS'))
print('')


#Testing CCACollection Class
print('Testing CCACollection Class')
c = CCACollection()
print(c)
print('')

cca1 = CCA('robotics', 'club')
record1 = vars(cca1)
print(f'Inserting record {record1}')
c.insert(record1)
print(c)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
c.insert(record1)
print(c)
print('')

cca2 = CCA('dragon boat', 'sports')
record2 = vars(cca2)
print(f'Inserting record {record2}')
c.insert(record2)
print(c)
print('')

cca1.type = 'societies'
new_record1 = vars(cca1)
print(f'Updating record {cca1.name} to {new_record1}')
c.update('robotics', new_record1)
print(c.find('robotics'))
print(c)
print('')

print(f'Deleting record {cca1.name}')
c.delete('robotics')
print(c)
print('')

print(f'Deleting record {cca2.name}')
c.delete('dragon boat')
print(c)
print('')

print(f'Finding record {cca1.name}(Should return none)')
print(c.find('robotics'))
print('')

print(f'Deleting record {cca1.name} again(Should give error)')
c.delete('robotics')
print('')


#Testing ActivityCollection Class
print('Testing ActivityCollection Class')
c = ActivityCollection()
print(c)
print('')

activity1 = Activity('NOI', '17 April 2023', '18 April 2023')
record1 = vars(activity1)
print(f'Inserting record {record1}')
c.insert(record1)
print(c)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
c.insert(record1)
print(c)
print('')

activity2 = Activity('AFA', '29 November 2022', '30 November 2022')
record2 = vars(activity2)
print(f'Inserting record {record2}')
c.insert(record2)
print(c)
print('')

activity1.end_date = '19 April 2023'
new_record1 = vars(activity1)
print(f'Updating record {activity1.description} to {new_record1}')
c.update('NOI', new_record1)
print(c.find('NOI'))
print(c)
print('')

print(f'Deleting record {activity1.description}')
c.delete('NOI')
print(c)
print('')

print(f'Deleting record {activity2.description}')
c.delete('AFA')
print(c)
print('')

print(f'Finding record {activity1.description}(Should return none)')
print(c.find('NOI'))
print('')

print(f'Deleting record {activity1.description} again(Should give error)')
c.delete('NOI')
print('')