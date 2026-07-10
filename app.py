from datetime import datetime

yr = datetime.today().year - 2000


class Student:
    NumberofStudent = 0
    Base_USN = "4DM"

    def __init__(self, name, Branch):
        Student.NumberofStudent += 1
        self._NumberofStudent = Student.NumberofStudent

        self._name = name
        self._Branch = Branch
        self._USN = (
            Student.Base_USN
            + str(yr)
            + self._Branch
            + str(self._NumberofStudent)
        )

        self._Attendence = 0
        self._today = None

    def Display(self, allMarks):
        print("=" * 80)
        print(f"Name : {self._name}")
        print(f"USN  : {self._USN}")

        if self._name in allMarks:
            for subject, mark in allMarks[self._name].items():
                print(f"{subject} : {mark}")

        print(f"Attendance : {self._Attendence}")
        print(f"Today      : {self._today}")
        print("=" * 80)
    
    def Dumpfile(self, system):
        if self._name not in system._studentDB:
            print("You entered the wrong name!")
            return

        self.file(system)

    def file(self, system):
        marks = system._Marks.get(self._name, {})
        with open(f"{self._name}.txt", "w") as f:
            f.write(f"""
                 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                 Name       : {self._name}
                 USN        : {self._USN}
                 Branch     : {self._Branch}
                 
                 Marks
                     Physics      : {TeacherManagementSystem()._Marks['physics']}
                     Chemistry    : {TeacherManagementSystem()._Marks['chemistry']}
                     Mathematics  : {TeacherManagementSystem()._Marks['maths']}
                 
                 Attendance : {self._Attendence}
                 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                 """)

        
        

   


class TeacherManagementSystem:
    def __init__(self):
        self._Marks = {}
        self._studentDB = {}

    def takeattendence(self):
        print("=" * 80)

        for student in self._studentDB.values():

            today = input(f"{student._name} Attendance [Present:p/Absent:a] : ")

            if today.lower().strip() == "p":
                student._today = "Present"
                student._Attendence += 1

            elif today.lower().strip() == "a":
                student._today = "Absent"

            else:
                print("Wrong Input")

        print("=" * 80)

    def _addstudent(self):
        print("_" * 80)

        name = input("Student Name : ")
        branch = input("Student Branch : ")

        student_obj = Student(name, branch)
        self._Marks[name] = {
            "Physics": 0,
            "Chemistry": 0,
            "Mathematics": 0,
            "Average": (0 + 0 + 0) / 3,
        }
        self._studentDB[name] = student_obj
        self.dumpmain(name)
        


        print("Student Added Successfully")
        print("_" * 80)

    def dumpmain(self,name):
        with open("students.txt", "a") as f:
            f.write(f"""
             ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
             Name       : {name}\n
             USN        : {self._studentDB[name]._USN}\n
             Branch     : {self._studentDB[name]._Branch}\n
             Marks:---------------------------------------------------------\n
                 Physics      : {self._Marks[name]['Physics']}\n
                 Chemistry    : {self._Marks[name]['Chemistry']}\n
                 Mathematics  : {self._Marks[name]['Mathematics']}\n
                 Avarage      : {self._Marks[name]["Average"]}\n
                 -------------------------------------------------------------\n
             Attendance : {self._studentDB[name]._Attendence}\n
             
             """)
    def specificDump(self,value):
        

    def _addMarks(self):
        print("_" * 80)

        name = input("Enter Student Name : ")

        if name not in self._studentDB:
            print("Student Not Found")
            return

        physics = int(input("Physics Marks : "))
        chemistry = int(input("Chemistry Marks : "))
        maths = int(input("Mathematics Marks : "))

        self._Marks[name] = {
            "Physics": physics,
            "Chemistry": chemistry,
            "Mathematics": maths,
            "Average": (physics + chemistry + maths) / 3,
        }

        print("Marks Added Successfully")
        print("_" * 80)

    def _updateMarks(self):
        print("_" * 80)

        name = input("Enter Student Name : ")

        if name not in self._Marks:
            print("Student Marks Not Found")
            return

        choose = input(
            "Enter Subject (Physics/Chemistry/Mathematics/All): "
        ).lower()

        if choose == "physics":
            self._Marks[name]["Physics"] = int(input("Physics Marks : "))

        elif choose == "chemistry":
            self._Marks[name]["Chemistry"] = int(input("Chemistry Marks : "))

        elif choose == "mathematics" or choose == "maths":
            self._Marks[name]["Mathematics"] = int(
                input("Mathematics Marks : ")
            )

        elif choose == "all":
            physics = int(input("Physics Marks : "))
            chemistry = int(input("Chemistry Marks : "))
            maths = int(input("Mathematics Marks : "))

            self._Marks[name] = {
                "Physics": physics,
                "Chemistry": chemistry,
                "Mathematics": maths,
                "Average": (physics + chemistry + maths) / 3,
            }

        self._Marks[name]["Average"] = (
            self._Marks[name]["Physics"]
            + self._Marks[name]["Chemistry"]
            + self._Marks[name]["Mathematics"]
        ) / 3

        print("Marks Updated Successfully")
        print("_" * 80)

    def _viewallStudent(self):
        if not self._studentDB:
            print("No Students Added")
            return

        for student in self._studentDB.values():
            student.Display(self._Marks)
    
    def _allintofile(self):
       
        for name,data in self._studentDB.items():
            with open("students.txt", "a") as f:
                f.write(f"""
                 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
                 Name       : {name}\n
                 USN        : {self._studentDB[name]._USN}\n
                 Branch     : {self._studentDB[name]._Branch}\n
                 Marks:---------------------------------------------------------\n
                     Physics      : {self._Marks[name]['Physics']}\n
                     Chemistry    : {self._Marks[name]['Chemistry']}\n
                     Mathematics  : {self._Marks[name]['Mathematics']}\n
                     Avarage      : {self._Marks[name]["Average"]}\n
                     -------------------------------------------------------------\n
                 Attendance : {self._studentDB[name]._Attendence}\n
                 
                 """)


class Engine:

    def __init__(self):
        self.sys = TeacherManagementSystem()
        
    def run(self):


        while True:

            print("=" * 80)
            print("1 : ADD Student")
            print("2 : ADD Student Marks")
            print("3 : Update Student Marks")
            print("4 : View All Students")
            print("5 : Take Attendance")
            print("6 : Student file")
            print("7 : All in to File")
            print("8 : Exit")
            print("=" * 80)

            choice = int(input("Your Choice : "))

            if choice == 1:
                self.sys._addstudent()

            elif choice == 2:
                self.sys._addMarks()

            elif choice == 3:
                self.sys._updateMarks()

            elif choice == 4:
                self.sys._viewallStudent()

            elif choice == 5:
                self.sys.takeattendence()

            elif choice==6:
                self.sys._allintofile()
            elif choice == 6:
                print("Thank You")
                break

            else:
                print("Invalid Choice")


obj = Engine()
obj.run()