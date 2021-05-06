"""Author: Bansri Patel
   Created: 4/10/2021
   Updated: 4/19/2021

   Purpose:
   create a data repository of courses, majors, students, and instructors
"""

import os
from HW08_Bansrikumari_Patel import file_reader
from typing import List, Iterator, Tuple, DefaultDict, Set, Dict
from collections import defaultdict
from prettytable import PrettyTable


class Student:
    """student class that has student CWID, Name, Completed courses and grades.
       It has methods to add course and grade and to return student information
    """
    st_field_names: List[str] = ["CWID", "Name", "Major", "Completed Courses",
                                 "Remaining Required", "Remaining Electives",
                                 "GPA"]

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """init method to initialize the attributes"""
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def add_course(self, course: str, grade: str) -> None:
        """method to add courses and grades"""
        self._courses[course] = grade

    def compute_gpa(self) -> float:
        """method to compute gpa"""
        grades: Dict[str, float] = {"A": 4.00, "A-": 3.75, "B+": 3.25,
                                    "B": 3.00, "B-": 2.75, "C+": 2.25,
                                    "C": 2.00, "C-": 0.00, "D+": 0.00,
                                    "D": 0.00, "D-": 0.00, "F": 0.00}
        try:
            total: float = sum([grades[grade] for grade in
                                self._courses.values()]) / len(self._courses.
                                                               values())
            return round(total, 2)
        except ZeroDivisionError as e:
            print(e)

    def st_data(self) -> Tuple[str, str, str, List[str], List[str],
                               List[str], float]:
        """returns student row"""
        major, passed, rem_required, rem_electives = self._major.\
            remaining_courses(self._courses)
        return [self._cwid, self._name, major, sorted(passed),
                sorted(rem_required), sorted(rem_electives),
                self.compute_gpa()]


class Instructor:
    """Instructor class has instructor CWID, name, department, courses and
       number of students who took that course. It has methods to increase
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


class Major:
    """Major class has required and elective courses and computes reamining
       required and remaining elective courses
    """
    major_field_names: List[str] = ["Major", "Required Courses", "Electives"]
    passing_grades: Set[str] = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def __init__(self, department: str) -> None:
        """init method to initialize the attributes"""
        self._department: str = department
        self._required: Set[str] = set()
        self._electives: Set[str] = set()

    def add_course(self, course: str, type_c: str) -> None:
        """add required and elective courses"""
        if type_c == 'R':
            self._required.add(course)
        elif type_c == 'E':
            self._electives.add(course)
        else:
            raise ValueError("Invalid course type")

    def remaining_courses(self, completed: Dict) -> Tuple[str, str, str, str]:
        """compute remaining required and elective courses"""
        completed: Dict = {course for course, grade in completed.items() if
                           grade in Major.passing_grades}

        rem_required: Set = self._required - completed
        rem_electives: Set = self._electives
        if self._electives.intersection(completed):
            rem_electives = set()

        return self._department, completed, rem_required, rem_electives

    def major_data(self) -> Tuple[str, List[str], List[str]]:
        """return majors row"""
        return (self._department, sorted(self._required),
                sorted(self._electives))


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
        self._majors_dict: Dict[str, Major] = dict()

        try:
            self._get_majors(os.path.join(dir_path, "majors.txt"))
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
                print("Majors Data")
                print(self.majors_pt())

    def _get_majors(self, path: str) -> None:
        """read majors data from file using file_reader into the container"""
        try:
            majors_data: Iterator(Tuple[str]) = file_reader(path, 3, sep="\t",
                                                            header=True)
            for major, flag, course in majors_data:
                if major not in self._majors_dict:
                    self._majors_dict[major] = Major(major)
                self._majors_dict[major].add_course(course, flag)
        except ValueError as v:
            print(v)

    def _get_students(self, path: str) -> None:
        """read students data from file into the container"""
        try:
            students_data: Iterator(Tuple[str]) = file_reader(path, 3,
                                                              sep=";",
                                                              header=True)
            for cwid, name, major in students_data:
                if major not in self._majors_dict:
                    print(f"Student {cwid} '{name}' has unknown major {major}")
                else:
                    self._students_dict[cwid] = Student(cwid, name, self.
                                                        _majors_dict[major])
        except ValueError as v:
            print(v)

    def _get_instructors(self, path: str) -> None:
        """read instructors data from file using file_reader into the container
        """
        try:
            instructors_data: Iterator(Tuple[str]) = file_reader(path, 3,
                                                                 sep="|",
                                                                 header=True)
            for cwid, name, department in instructors_data:
                self._instructors_dict[cwid] = Instructor(cwid, name,
                                                          department)
        except ValueError as v:
            print(v)

    def _get_grades(self, path: str) -> None:
        """read data of grades from grades file and update student and
           instructor data.
        """
        grades: Iterator(Tuple[str]) = file_reader(path, 4, sep="|",
                                                   header=True)
        for st_cwid, course, grade, inst_cwid in grades:
            if st_cwid in self._students_dict:
                self._students_dict[st_cwid].add_course(course, grade)
            else:
                print(f"grade for unknown student {st_cwid}")
            if inst_cwid in self._instructors_dict:
                self._instructors_dict[inst_cwid].update_students(course)
            else:
                print(f"grade for unkown instructor {inst_cwid}")

    def student_pt(self) -> PrettyTable:
        """print pretty table for student"""
        p_table: PrettyTable = PrettyTable(field_names=Student.st_field_names)

        for student in self._students_dict.values():
            p_table.add_row(student.st_data())

        return p_table

    def instructor_pt(self) -> PrettyTable:
        """print pretty table for instructor"""
        p_table: PrettyTable = PrettyTable(field_names=Instructor.
                                           inst_field_names)

        for instructor in self._instructors_dict.values():
            for row in instructor.inst_data():
                p_table.add_row(row)

        return p_table

    def majors_pt(self) -> PrettyTable:
        """print pretty table for major"""
        p_table: PrettyTable = PrettyTable(field_names=Major.major_field_names)

        for major in self._majors_dict.values():
            p_table.add_row(major.major_data())

        return p_table


def main() -> None:
    """create object of Repository"""
    rp: Repository = Repository("/Users/bansripatel/Desktop/ssw-810", True)


if __name__ == "__main__":
    main()
