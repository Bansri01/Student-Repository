"""Author: Bansri Patel
   Created: 4/10/2021

   Purpose:
   create a data repository of courses, students, and instructors
"""

import os
from HW08_Bansrikumari_Patel import file_reader
from typing import List, Iterator, Tuple, DefaultDict
from collections import defaultdict
from prettytable import PrettyTable


class Student:
    """student class that has student CWID, Name, Completed courses and grades.
       It has methods to add course and grade and to return student information
    """
    st_field_names: List[str] = ["CWID", "Name", "Completed Courses"]

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """init method to initialize the attributes"""
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def add_course(self, course: str, grade: str) -> None:
        """method to add courses and grades"""
        self._courses[course] = grade

    def st_data(self) -> Tuple[str, str, List[str]]:
        """returns student row"""
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """Instructor class has instructor CWID, name, department, courses and
       numberof students who took that course. It has methods to increase
       number of students who took their course and to return instructor
       information
    """

    inst_field_names: List[str] = ["CWID", "Name", "Dept", "Courses",
                                   "Students"]

    def __init__(self, cwid: str, name: str, department: str) -> None:
        """init method to initialize the attributes"""
        self._cwid: str = cwid
        self._name: str = name
        self._department: str = department
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def update_students(self, course: str) -> None:
        """method to increament number of students for a course"""
        self._courses[course] += 1

    def inst_data(self) -> Iterator[Tuple[str, str, str, str, int]]:
        """returns instructor row"""
        for course, students in self._courses.items():
            yield [self._cwid, self._name, self._department, course, students]


class Repository:
    """Repository class has all the information. It reads data from student,
       instructor and grade files and print pretty tables for students and
       instructors
    """

    def __init__(self, dir_path: str, tables: bool = True) -> None:
        """init method to initialize the attributes"""
        self._dir_path: str = dir_path
        self._students_dict: Dict[str, Student] = dict()
        self._instructors_dict: Dict[str, Instructor] = dict()

        try:
            self._get_students(os.path.join(dir_path, "students.txt"))
            self._get_instructors(os.path.join(dir_path, "instructors.txt"))
            self._get_grades(os.path.join(dir_path, "grades.txt"))
        except FileNotFoundError:
            raise FileNotFoundError("Invalid Path,\
                                    file not found at this path")
        except ValueError as v:
            print(v)
        else:
            if tables:
                print("Student Data")
                print(self.student_pt())
                print("Instructor Data")
                print(self.instructor_pt())

    def _get_students(self, path: str) -> None:
        """read students data from file into the container"""
        try:
            students_data: Iterator(Tuple[str]) = file_reader(path, 3,
                                                              sep="\t",
                                                              header=False)
            for cwid, name, major in students_data:
                self._students_dict[cwid] = Student(cwid, name, major)
        except ValueError as v:
            raise ValueError(v)

    def _get_instructors(self, path: str) -> None:
        """read instructors data from file using file_reader into the container
        """
        try:
            instructors_data: Iterator(Tuple[str]) = file_reader(path, 3,
                                                                 sep="\t",
                                                                 header=False)
            for cwid, name, department in instructors_data:
                self._instructors_dict[cwid] = Instructor(cwid, name,
                                                          department)
        except ValueError as v:
            raise ValueError(v)

    def _get_grades(self, path: str) -> None:
        """read data of grades from grades file and update student and
           instructor data.
        """
        grades: Iterator(Tuple[str]) = file_reader(path, 4, sep="\t",
                                                   header=False)
        for st_cwid, course, grade, inst_cwid in grades:
            if st_cwid in self._students_dict:
                self._students_dict[st_cwid].add_course(course, grade)
            else:
                print(f"grade for unknown student {st_cwid}")
            if inst_cwid in self._instructors_dict:
                self._instructors_dict[inst_cwid].update_students(course)
            else:
                print(f"grade for unkown instructor {inst_cwid}")

    def student_pt(self) -> None:
        """print pretty table for student"""
        p_table: PrettyTable = PrettyTable(field_names=Student.st_field_names)

        for student in self._students_dict.values():
            p_table.add_row(student.st_data())

        return p_table

    def instructor_pt(self) -> None:
        """print pretty table for instructor"""
        p_table: PrettyTable = PrettyTable(field_names=Instructor.
                                           inst_field_names)

        for instructor in self._instructors_dict.values():
            for row in instructor.inst_data():
                p_table.add_row(row)

        return p_table


def main() -> None:
    """create object of Repository"""
    rp: Repository = Repository("/Users/bansripatel/Desktop/ssw-810", True)


if __name__ == "__main__":
    main()
