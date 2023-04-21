class Student:
    def __init__(self, name, age, year_enrolled, graduating_year):
        self.name = name
        self.age = age
        self.year_enrolled = year_enrolled
        self.graduating_year = graduating_year

    def __repr__(self):
        return f'Student object\nName: {self.name}, Age: {self.age}, Year Enrolled: {self.year_enrolled}, Graduating Year: {self.graduating_year}'


class Class:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'Class object\nName: {self.name}, Level: {self.level}'


class Subject:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def __repr__(self):
        return f'Subject object\nName: {self.name}, Level: {self.level}'


class CCA:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def __repr__(self):
        return f'CCA object\nName: {self.name}, Type: {self.type}'


class Activity:
    def __init__(self, start_date, end_date, description):
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        
    def __repr__(self):
        return f'Activity object\nStart Date: {self.start_date}, End Date: {self.end_date}, Description: {self.description}'


class Collection:
    def __init__():
        pass

class StudentCollection(Collection):
    pass

class CCACollection(Collection):
    pass

class SubjectCollection(Collection):
    pass

class ClassCollection(Collection):
    pass

class ActivityCollection(Collection):
    pass