import sqlite3

class Student:
    def __init__(self, name, age, year_enrolled, graduating_year, class_):
        self.name = name
        self.age = int(age)
        self.year_enrolled = int(year_enrolled)
        self.graduating_year = int(graduating_year)
        self.class_ = class_

    def __repr__(self):
        return f'Student object\nName: {self.name}, Age: {self.age}, Year Enrolled: {self.year_enrolled}, Graduating Year: {self.graduating_year}, Class: {self.class_}'


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


class StudentSubject:
    def __init__(self, student_name, subject_name):
        self.student_name = student_name
        self.subject_name = subject_name

    def __repr__(self):
        return f'Student-Subject object\nStudent Name: {self.student_name}, Subject Name: {self.subject_name}'


class CCA:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def __repr__(self):
        return f'CCA object\nName: {self.name}, Type: {self.type}'


class StudentCCA:
    def __init__(self, student_name, cca_name, role):
        self.student_name = student_name
        self.cca_name = cca_name
        self.role = role

    def __repr__(self):
        return f'Student-CCA object\nStudent Name: {self.student_name}, CCA Name: {self.cca_name}, Role: {self.role}'

    
class Activity:
    def __init__(self, description, start_date, end_date, ):
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
         
    def __repr__(self):
        return f'Activity object\nDescription: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}'


class StudentActivity:
    def __init__(self, student_name, activity_description, category, role, award, hours):
        self.student_name = student_name
        self.activity_description = activity_description
        self.category = category
        self.role = role
        self.award = award
        self.hours = int(hours)

    def __repr__(self):
        return f'Student-Activity object\nStudent Name: {self.student_name}, Activity Description: {self.activity_description}, Category: {self.category}, Role: {self.role}, Award: {self.award}, Hours: {self.hours}'


def remove_quotes_in_tuple(tuple):
    string = '('
    for element in tuple:
        string += element
        string += ', '
    string = string.strip(', ')
    string += ')'

    return string
    
def generate_placeholder_string(n):
    tuple = ('?',)*n
    string = remove_quotes_in_tuple(tuple)
    
    return string

class Collection:
    """
    Models a Collection of records using SQLite3

    Attributes:
    (-) `dbname`: the sqlite Database filename
    (-) `tblname`: the name of the table we will be using

    Methods:
    (+) `insert(record)`: Inserts a record into the collection, after checking whether it is present.
    (+) `find(name)`: Find the record with matching name, and returns a copy of it.
    (+) `findall()`: Returns all the records in the data attribute.
    (+) `update(name, record)`: Update the record with matching name, by replacing it's elements with the given record.
    (+) `delete(name)`: Deletes the record with matching name.
    """
    def __init__(self, dbname, tblname, primary_key):
        self.dbname = dbname
        self.tblname = tblname
        self.primary_key = primary_key
        
        self.clear()

    
    def __repr__(self):
        return f"{self.tblname} table under {self.dbname} database(SQLite3).\nContains the following data:\n{str(self.findall())}"

    
    def _execute(self, query, **kwargs):
        print(query)
        print(f"Params: {kwargs.get('params')}")
        print('')
        
        conn = sqlite3.connect(self.dbname)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        #DQL
        if 'fetch' in kwargs:
            result = None
        
            if kwargs['fetch'] == 'one':
                c.execute(query, kwargs['params'])
                result = c.fetchone()
            elif kwargs['fetch'] == 'all':
                c.execute(query)
                result = c.fetchall()

            return result
            
        #DML
        else:
            
            c.execute(query, kwargs['params'])
            conn.commit()
            
        conn.close()

        
    def clear(self):
        query = f"""                         
                 DROP TABLE IF EXISTS {self.tblname}
                 """
        
        with sqlite3.connect(self.dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()

    
    def find(self, key_value):
        if not isinstance(self.primary_key, tuple):
            primary_key_string = self.primary_key
            placeholder_string = '?'
            params = (key_value,)
            
        else:
            primary_key_string = remove_quotes_in_tuple(self.primary_key)
            placeholder_string = generate_placeholder_string(len(self.primary_key))
            params = key_value
            
        query = f"""           
                 SELECT * FROM {self.tblname}    
                 WHERE {primary_key_string} = {placeholder_string};
                 """

        result = self._execute(query, params = params, fetch = 'one')
        
        if result is not None:
            print(f'Search result: {dict(result)}')
            return dict(result)
            
        print(f'Search result: None')
        return None
        
    
    def findall(self):
        query = f"""                            
                 SELECT * FROM {self.tblname}        
                 """
        result = self._execute(query, fetch = 'all')
        if result != []:
            return [dict(row) for row in result]
        return None

        
    def insert(self, record):
        if not isinstance(self.primary_key, tuple):
            key_value = record[self.primary_key]
        else:
            key_value = tuple(record[key] for key in tuple(self.primary_key))
            
        result = self.find(key_value)
            
        if result is not None:
            print('Record is already present!')
        else:
            placeholder_string = generate_placeholder_string(len(record))
            query = f"""                        
                     INSERT INTO {self.tblname}
                     VALUES {placeholder_string};       
                     """
            params = tuple(record.values())
            self._execute(query, params = params)

    
    def delete(self, key_value):
        result = self.find(key_value)
        if result is None:
            print('Record not found!')
        else:
            if not isinstance(self.primary_key, tuple):
                primary_key_string = self.primary_key
                placeholder_string = '?'
                params = (key_value,)
            else:
                primary_key_string = remove_quotes_in_tuple(self.primary_key)
                placeholder_string = generate_placeholder_string(len(self.primary_key))
                params = key_value
                
            query = f"""                       
                     DELETE FROM {self.tblname} 
                     WHERE {primary_key_string} = {placeholder_string};  
                     """
            
            self._execute(query, params = params)

            
    def update(self, key_value, record):
        result = self.find(key_value)
        if result is None:
            print('Record not found!')
        else:
            keys = list(record.keys())
            update_string = ','.join([f'"{key}" = ?' for key in keys])
            params = tuple(record.values()) 
            
            if not isinstance(self.primary_key, tuple):
                primary_key_string = self.primary_key
                key_value_string = f"'{key_value}'"
            else:
                primary_key_string = remove_quotes_in_tuple(self.primary_key)
                key_value_string = key_value
            
            query = f"""                        
                     UPDATE {self.tblname}          
                     SET {update_string}         
                     WHERE {primary_key_string} = {key_value_string};
                     """
            self._execute(query, params=params)


class StudentCollection(Collection):
    def __init__(self):
        self._tblname = 'students'
        self._dbname = 'mywebapp.db'
        self.primary_key = 'name'
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'name' TEXT,
                    'age' INT,
                    'year_enrolled' INT,
                    'graduating_year' INT,
                    'class_' TEXT,
                    PRIMARY KEY('name')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()


class ClassCollection(Collection):
    def __init__(self):
        self._tblname = 'classes'
        self._dbname = 'mywebapp.db'
        self.primary_key = 'name'
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'name' TEXT,
                    'level' TEXT,
                    PRIMARY KEY('name')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()


class SubjectCollection(Collection):
    def __init__(self):
        self._tblname = 'subjects'
        self._dbname = 'mywebapp.db'
        self.primary_key = 'name'
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'name' TEXT,
                    'level' TEXT,
                    PRIMARY KEY('name')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()


class StudentSubjectCollection(Collection):
    def __init__(self):
        self._tblname = 'studentsubjects'
        self._dbname = 'mywebapp.db'
        self.primary_key = ('student_name', 'subject_name')
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'student_name' TEXT,
                    'subject_name' TEXT,
                    PRIMARY KEY('student_name', 'subject_name')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()


class CCACollection(Collection):
    def __init__(self):
        self._tblname = 'CCAs'
        self._dbname = 'mywebapp.db'
        self.primary_key = 'name'
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'name' TEXT,
                    'type' TEXT,
                    PRIMARY KEY('name')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()


class StudentCCACollection(Collection):
    pass


class ActivityCollection(Collection):
    def __init__(self):
        self._tblname = 'activities'
        self._dbname = 'mywebapp.db'
        self.primary_key = 'description'
        
        super().__init__(self._dbname, self._tblname, self.primary_key)
        self._create_table()
        
    def _create_table(self):
        query = f"""
                 CREATE TABLE IF NOT EXISTS 
                 '{self._tblname}'(
                    'description' TEXT,
                    'start_date' TEXT,
                    'end_date' TEXT,
                    PRIMARY KEY('description')
                 ); 
                 """
        with sqlite3.connect(self._dbname) as conn:
            cur = conn.cursor()
            cur.execute(query)
            # conn.close()

class StudentActivityCollection(Collection):
    pass