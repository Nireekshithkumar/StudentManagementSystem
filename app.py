from datetime import datetime
import json
import os

yr = datetime.today().year - 2000


class Student:
    NumberofStudent = 0
    Base_USN = "4DM"

    def __init__(self, name, branch):
        Student.NumberofStudent += 1
        self._NumberofStudent = Student.NumberofStudent
        self._name = name
        self._Branch = branch
        self._USN = Student.Base_USN + \
            str(yr) + self._Branch + str(self._NumberofStudent)
        self._Attendence = 0
        self._today = "Not Taken"

    def Display(self, allMarks):
        print("=" * 80)
        print(f"Name : {self._name}")
        print(f"USN  : {self._USN}")
        print(f"Branch : {self._Branch}")
        print(f"Attendance : {self._Attendence}")
        print(f"Today      : {self._today}")
        if self._name.lower() in allMarks:
            for subject, mark in allMarks[self._name.lower()].items():
                print(f"{subject} : {mark}")
        print("=" * 80)


class TeacherManagementSystem:
    def __init__(self):
        self._Marks = {}
        self._studentDB = {}
        self._teacherDB = {}
        self._teacher_file = "teacher_db.json"
        self._student_file = "student_db.json"
        self._load_teacher_db()
        self._load_student_db()

    def _load_teacher_db(self):
        if os.path.exists(self._teacher_file):
            with open(self._teacher_file, "r") as handle:
                self._teacherDB = json.load(handle)
        else:
            self._teacherDB = {"principle": "1234"}
            self._save_teacher_db()

    def _save_teacher_db(self):
        with open(self._teacher_file, "w") as handle:
            json.dump(self._teacherDB, handle, indent=2)

    def _load_student_db(self):
        if os.path.exists(self._student_file):
            with open(self._student_file, "r") as handle:
                raw_data = json.load(handle)
            self._studentDB = raw_data
            self._Marks = {
                key: data.get("marks", {
                    "Physics": 0,
                    "Chemistry": 0,
                    "Mathematics": 0,
                    "Average": 0,
                })
                for key, data in self._studentDB.items()
            }
        else:
            self._studentDB = {}
            self._Marks = {}

    def _save_student_db(self):
        with open(self._student_file, "w") as handle:
            json.dump(self._studentDB, handle, indent=2)

    def authenticate_teacher(self, username, password):
        return self._teacherDB.get(username.strip().lower()) == password.strip()

    def authenticate_student(self, name, usn):
        student_key = name.strip().lower()
        student_data = self._studentDB.get(student_key)
        if not student_data:
            return None
        return student_data if student_data.get("usn") == usn.strip().upper() else None

    def takeattendence(self):
        print("=" * 80)
        for key, student_data in self._studentDB.items():
            today = input(
                f"{student_data['name']} Attendance [Present:p/Absent:a] : ").strip().lower()
            if today in {"p", "present"}:
                student_data["today"] = "Present"
                student_data["attendance"] += 1
            elif today in {"a", "absent"}:
                student_data["today"] = "Absent"
            else:
                print("Wrong Input")
        self._save_student_db()
        print("=" * 80)

    def _addstudent(self):
        print("_" * 80)
        name = input("Student Name : ").strip()
        branch = input("Student Branch : ").strip()
        student_obj = Student(name, branch)
        student_key = name.lower()
        self._studentDB[student_key] = {
            "name": name,
            "branch": branch,
            "usn": student_obj._USN,
            "attendance": student_obj._Attendence,
            "today": student_obj._today,
            "marks": {
                "Physics": 0,
                "Chemistry": 0,
                "Mathematics": 0,
                "Average": 0,
            },
        }
        self._Marks[student_key] = self._studentDB[student_key]["marks"]
        self._save_student_db()
        self.dumpmain(student_key)
        print("Student Added Successfully")
        print("_" * 80)

    def dumpmain(self, student_key):
        student_data = self._studentDB[student_key]
        with open("students.txt", "a") as handle:
            handle.write(
                f"""
             ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
             Name       : {student_data['name']}\n
             USN        : {student_data['usn']}\n
             Branch     : {student_data['branch']}\n
             Marks:---------------------------------------------------------\n
                 Physics      : {student_data['marks']['Physics']}\n
                 Chemistry    : {student_data['marks']['Chemistry']}\n
                 Mathematics  : {student_data['marks']['Mathematics']}\n
                 Average      : {student_data['marks']['Average']}\n
                 -------------------------------------------------------------\n
             Attendance : {student_data['attendance']}\n
             """
            )

    def _addteacher(self):
        print("_" * 80)
        username = input("New Teacher Username : ").strip().lower()
        password = input("New Teacher Password : ").strip()
        self._teacherDB[username] = password
        self._save_teacher_db()
        print("Teacher Added Successfully")
        print("_" * 80)

    def _addMarks(self):
        print("_" * 80)
        name = input("Enter Student Name : ").strip()
        student_key = name.lower()
        if student_key not in self._studentDB:
            print("Student Not Found")
            return
        physics = int(input("Physics Marks : "))
        chemistry = int(input("Chemistry Marks : "))
        maths = int(input("Mathematics Marks : "))
        self._studentDB[student_key]["marks"] = {
            "Physics": physics,
            "Chemistry": chemistry,
            "Mathematics": maths,
            "Average": (physics + chemistry + maths) / 3,
        }
        self._Marks[student_key] = self._studentDB[student_key]["marks"]
        self._save_student_db()
        print("Marks Added Successfully")
        print("_" * 80)

    def _updateMarks(self):
        print("_" * 80)
        name = input("Enter Student Name : ").strip()
        student_key = name.lower()
        if student_key not in self._studentDB:
            print("Student Marks Not Found")
            return
        choose = input(
            "Enter Subject (Physics/Chemistry/Mathematics/All): ").strip().lower()
        marks = self._studentDB[student_key]["marks"]
        if choose == "physics":
            marks["Physics"] = int(input("Physics Marks : "))
        elif choose == "chemistry":
            marks["Chemistry"] = int(input("Chemistry Marks : "))
        elif choose in {"mathematics", "maths"}:
            marks["Mathematics"] = int(input("Mathematics Marks : "))
        elif choose == "all":
            marks["Physics"] = int(input("Physics Marks : "))
            marks["Chemistry"] = int(input("Chemistry Marks : "))
            marks["Mathematics"] = int(input("Mathematics Marks : "))
        else:
            print("Invalid subject")
            return
        marks["Average"] = (marks["Physics"] +
                            marks["Chemistry"] + marks["Mathematics"]) / 3
        self._Marks[student_key] = marks
        self._save_student_db()
        print("Marks Updated Successfully")
        print("_" * 80)

    def _viewallStudent(self):
        if not self._studentDB:
            print("No Students Added")
            return
        for name, student_data in self._studentDB.items():
            student_obj = Student(student_data["name"], student_data["branch"])
            student_obj._USN = student_data["usn"]
            student_obj._Attendence = student_data["attendance"]
            student_obj._today = student_data["today"]
            student_obj.Display({name: self._Marks.get(name, {})})

    def _allintofile(self):
        for student_key, student_data in self._studentDB.items():
            with open("students.txt", "a") as handle:
                handle.write(
                    f"""
                 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
                 Name       : {student_data['name']}\n
                 USN        : {student_data['usn']}\n
                 Branch     : {student_data['branch']}\n
                 Marks:---------------------------------------------------------\n
                     Physics      : {student_data['marks']['Physics']}\n
                     Chemistry    : {student_data['marks']['Chemistry']}\n
                     Mathematics  : {student_data['marks']['Mathematics']}\n
                     Average      : {student_data['marks']['Average']}\n
                     -------------------------------------------------------------\n
                 Attendance : {student_data['attendance']}\n
                 """
                )

    def _show_student_info(self, student_key):
        student_data = self._studentDB[student_key]
        print("=" * 80)
        print(f"Name : {student_data['name']}")
        print(f"USN  : {student_data['usn']}")
        print(f"Branch : {student_data['branch']}")
        print(f"Attendance : {student_data['attendance']}")
        print(f"Today : {student_data['today']}")
        print("=" * 80)

    def _show_student_marks(self, student_key):
        student_data = self._studentDB[student_key]
        print("=" * 80)
        for subject, mark in student_data["marks"].items():
            print(f"{subject} : {mark}")
        print("=" * 80)


class StudentView:
    def __init__(self, system):
        self.sys = system

    def run(self):
        while True:
            name = input("Student Name : ").strip()
            usn = input("USN : ").strip()
            student_data = self.sys.authenticate_student(name, usn)
            if student_data:
                print("Student login successful")
                self._student_menu(name.lower())
                break
            print("Student not found in database")
            again = input("Try again? [y/n] : ").strip().lower()
            if again != "y":
                break

    def _student_menu(self, student_key):
        while True:
            print("=" * 80)
            print("1 : View My Details")
            print("2 : View My Marks")
            print("3 : Exit")
            print("=" * 80)
            choice = input("Your Choice : ").strip()
            if choice == "1":
                self.sys._show_student_info(student_key)
            elif choice == "2":
                self.sys._show_student_marks(student_key)
            elif choice == "3":
                print("Thank You")
                break
            else:
                print("Invalid Choice")
        


class TeacherView:
    def __init__(self, system):
        self.sys = system

    def run(self):
        while True:
            username = input("Teacher Username : ").strip()
            password = input("Teacher Password : ").strip()
            if self.sys.authenticate_teacher(username, password):
                print("Teacher login successful")
                self._teacher_menu()
                break
            print("Invalid teacher name or password")
            again = input("Try again? [y/n] : ").strip().lower()
            if again != "y":
                break

    def _teacher_menu(self):
        while True:
            print("=" * 80)
            print("1 : Add Student")
            print("2 : Add Student Marks")
            print("3 : Update Student Marks")
            print("4 : View All Students")
            print("5 : Take Attendance")
            print("6 : Save All to File")
            print("7 : Add Another Teacher")
            print("8 : Exit")
            print("=" * 80)
            choice = input("Your Choice : ").strip()
            if choice == "1":
                self.sys._addstudent()
            elif choice == "2":
                self.sys._addMarks()
            elif choice == "3":
                self.sys._updateMarks()
            elif choice == "4":
                self.sys._viewallStudent()
            elif choice == "5":
                self.sys.takeattendence()
            elif choice == "6":
                self.sys._allintofile()
            elif choice == "7":
                self.sys._addteacher()
            elif choice == "8":
                print("Thank You")
                break
            else:
                print("Invalid Choice")


class Engine:
    def __init__(self):
        self.sys = TeacherManagementSystem()

    def run(self):
        while True:
            print("=" * 80)
            print("Enter your role: Teacher / Student / Exit")
            role = input("Your choice : ").strip().lower()
            if role in {"teacher", "t"}:
                TeacherView(self.sys).run()
            elif role in {"student", "s"}:
                StudentView(self.sys).run()
            elif role in {"exit", "e", "q"}:
                print("Thank You")
                break
            else:
                print("Invalid role")


if __name__ == "__main__":
    obj = Engine()
    obj.run()
