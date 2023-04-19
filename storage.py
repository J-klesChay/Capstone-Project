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