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
        self._login=datetime.now().today()
    
    def Display(self,allMarks):
        print("="*80)
        print(f"Name  : {self._name}")
        print(f" USN :{self._USN}")
        
        if self._name in allMarks:
            for subject,mark in allMarks[self._name].items():
                print(f"{subject} : {mark}")

        print(f" Login : {self._login}")
        print(f"Status :{["Present" if self._login==datetime.now().today() else "Absent"]}")
        print("="*80)
        

class Teacher(Student):
    def __init__(self, name, USN):
        super().__init__(name,USN)
        self._Marks={}
    
    def addMarks(self):
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
        
    
    

s1=Student("nireekshith","ECE")
s2=Teacher("nireekshith","4DM26ECE0")
print(s1._USN)
print(s2.addMarks())