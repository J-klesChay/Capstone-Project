test = str(("?",)*5)

test = test.replace('"', '')
print(test)
    
print(test)
from storage import *
#Testing storage classes
student = Student('Gary', '17', '2022', '2023', '2227')
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

#Testing StudentCollection Class
print('Testing StudentCollection Class')
s = StudentCollection()
print(s)
print('')

record1 = vars(student)
print(f'Inserting record {record1}')
s.insert(record1)
print(s)
print('')

print(f'Inserting record {record1} again\n(Should give error)')
s.insert(record1)
print(s)
print('')

student2 = Student('Jkles', '17', '2022', '2023', '2227')
record2 = vars(student2)
print(f'Inserting record {record2}')
s.insert(record2)
print(s)
print('')

student.class_ = 1234
new_record1 = vars(student)
print(f'Updating record Gary to {new_record1}')
s.update('Gary', new_record1)
print(s.find('Gary'))
print(s)
print('')

print('Deleting record Gary')
s.delete('Gary')
print(s)
print('')

print('Deleting record Jkles')
s.delete('Jkles')
print(s)
print('')

print('Finding record Gary(Should return none)')
print(s.find('Gary'))
print('')

print('Deleting record Gary again(Should give error)')
s.delete('Gary')