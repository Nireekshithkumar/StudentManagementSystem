from random import randint
from datetime import datetime

yr=datetime.today().year-2000

class Student:
    NumberofStudent=0
    Base_USN="4DM"
    def __init__(self,name,Branch):
        self._name=name
        self._NumberofStudent=Student.NumberofStudent+1
        self._Branch=Branch
        self._USN=Student.Base_USN+str(yr)+self._Branch+str(self.NumberofStudent)
        self._login=datetime.today()
        
    def Display(self,allMarks):
        print("="*80)
        print(f"Name  : {self._name}")
        print(f" USN :{self._USN}")
        
        if self._name in allMarks:
            for subject,mark in allMarks[self._name].items():
                print(f"{subject} : {mark}")

        print(f" Login : {self._login}")
        print(f"Status :{["Present" if self._login==datetime.today() else "Absent"]}")
        print("="*80)
        

class Teacher(Student):
    def __init__(self, name, USN):
        super().__init__(name,USN)
        self._Marks={}
        self._studentDB={}
    
    def takeattendence(self):
        


        
    
    def _addstudent(self):
        print('_'*80)
        name=input("Student Name:")
        branch=input("student Branch")
        student_obj=Student(name,branch)
        self._studentDB[name]={
            "USN":student_obj._USN,
            "Branch":student_obj._Branch,
            "Marks":self._Marks[self._name],
            "Last_login":student_obj._login,
            "status":{["Present" if self._login==datetime.today() else "Absent"]}
                                    }
        print('_'*80)
        return self._studentDB[self._name]
    
    def _addMarks(self):
        print('_'*80)
        physics=int(input("Phisics Marks="))
        chemistry=int(input("Chemistry Marks="))
        maths=int(input("maths Marks="))
        print('_'*80)

        self._Marks[self._name]={
            "Physics":physics,
            "Chemistry":chemistry,
            "Mathematics":maths,
            "Avarage":(physics+chemistry+maths)/3
        }
        return {self._name:
                self._Marks[self._name]}
    
    def _updateMarks(self):
        print('_'*80)
        choose=input("Enter which mark you whant to update")
        if choose.lower().strip()=="physics":
            physics=int(input("Phisics Marks="))
        elif choose.lower().strip()=="chemistry":
            chemistry=int(input("Chemistry Marks="))
        elif choose.lower().strip()=="maths":
            maths=int(input("maths Marks="))
        else:
            if choose.lower().strip()=="all":
                self._addMarks()
        print("The marks are Updated")
        print('_'*80)
        
    def _viewallStudent(self,allMarks):
        super().Display(allMarks)

        if self._studentDB:
            for student in self._studentDB:
                student.Display(allMarks)
    
                

    

s1=Student("nireekshith","ECE")
s1=Student("kumr","ECE")
s1=Student("nan","ECE")
s2=Teacher("pick","4DM26ECE0")
print(s2._Marks)
print(s1._USN)
print(s2._addMarks())
print(s2._viewallStudent(s2._Marks))