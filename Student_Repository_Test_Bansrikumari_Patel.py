"""Author: Bansri Patel
   Created: 4/10/2021
   Updated: 4/27/2021

   Purpose:
   To test the Major, Repository, Student and instructor class
"""

import unittest
import sqlite3
import os
from typing import Iterator, Tuple, Dict, List
from Student_Repository_Bansrikumari_Patel import Student, Instructor, Repository, Major


class TestMajor(unittest.TestCase):
    """Testing Major class"""
    def test_major(self) -> None:
        """test cases to test Major class"""
        self.path1: str = "/Users/bansripatel/Desktop/ssw-810"
        self.path2: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/810_startup.db")
        self.rt: Repository = Repository(self.path1, self.path2, False)
        table3: List[Tuple(str, List[str], List[str])] = [majors.major_data()
                                                          for majors in self.
                                                          rt._majors_dict.
                                                          values()
                                                          ]
        m_table: List[Tuple(str, List[str],
                      List[str])] = [('SFEN', ['SSW 540', 'SSW 555',
                                               'SSW 810'], ['CS 501',
                                                            'CS 546']),
                                     ('CS', ['CS 546', 'CS 570'], ['SSW 565',
                                                                   'SSW 810'])]
        self.assertEqual(m_table, table3)


class TestStudent(unittest.TestCase):
    """Testing Student class"""
    def test_student(self) -> None:
        """test cases to test Student class"""
        self.path1: str = "/Users/bansripatel/Desktop/ssw-810"
        self.path2: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/810_startup.db")
        self.rt: Repository = Repository(self.path1, self.path2, False)
        table1: List[List[str, str, str, List[str],
                     List[str], List[str], float]] = [student.st_data() for
                                                      cwid, student in self.rt.
                                                      _students_dict.items()]
        st_table: List[List[str, str, str, List[str],
                       List[str], List[str], float]] = [['10103', 'Jobs, S',
                                                         'SFEN', ['CS 501',
                                                                  'SSW 810'],
                                                         ['SSW 540', 'SSW 555'
                                                          ], [], 3.38],
                                                        ['10115', 'Bezos, J',
                                                         'SFEN', ['SSW 810'],
                                                         ['SSW 540',
                                                          'SSW 555'],
                                                         ['CS 501', 'CS 546'],
                                                         2.0],
                                                        ['10183', 'Musk, E',
                                                         'SFEN', ['SSW 555',
                                                                  'SSW 810'],
                                                         ['SSW 540'],
                                                         ['CS 501', 'CS 546'
                                                          ], 4.0],
                                                        ['11714', 'Gates, B',
                                                         'CS', ['CS 546',
                                                                'CS 570',
                                                                'SSW 810'], [],
                                                         [], 3.5]]

        self.assertEqual(st_table, table1)


class TestInstructor(unittest.TestCase):
    """Testing Instructor class"""
    def test_instructor(self) -> None:
        """Test cases to test Instructor class"""
        self.path1: str = "/Users/bansripatel/Desktop/ssw-810"
        self.path2: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/810_startup.db")
        self.rt: Repository = Repository(self.path1, self.path2, False)
        table2: set[Tuple[str, str, str, str, int]] = {tuple(inst_t) for
                                                       instructor in
                                                       self.rt.
                                                       _instructors_dict.
                                                       values() for inst_t
                                                       in instructor.
                                                       inst_data()}
        inst_table: set[Tuple[str, str, str, str,
                              int]] = {('98764', 'Cohen, R', 'SFEN', 'CS 546',
                                        1),
                                       ('98763', 'Rowland, J', 'SFEN',
                                        'SSW 810', 4),
                                       ('98763', 'Rowland, J', 'SFEN',
                                        'SSW 555', 1),
                                       ('98762', 'Hawking, S', 'CS',
                                        'CS 501', 1),
                                       ('98762', 'Hawking, S', 'CS',
                                        'CS 546', 1),
                                       ('98762', 'Hawking, S', 'CS',
                                        'CS 570', 1)}

        self.assertEqual(inst_table, table2)


class TestGradeSummary(unittest.TestCase):
    """Testing Student Grade Summary"""
    def test_Grade_Summary(self):
        """test cases to test student grade summary"""
        self.path1: str = "/Users/bansripatel/Desktop/ssw-810"
        self.path2: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/810_startup.db")
        self.rt: Repository = Repository(self.path1, self.path2, False)
        """Test cases to test Grade Summary"""
        table4: List[List[str, str, str, str,
                          str]] = [['Bezos, J', '10115', 'SSW 810', 'A',
                                    'Rowland, J'],
                                   ['Bezos, J', '10115', 'CS 546', 'F',
                                    'Hawking, S'],
                                   ['Gates, B', '11714', 'SSW 810', 'B-',
                                    'Rowland, J'],
                                   ['Gates, B', '11714', 'CS 546', 'A',
                                    'Cohen, R'],
                                   ['Gates, B', '11714', 'CS 570', 'A-',
                                    'Hawking, S'],
                                   ['Jobs, S', '10103', 'SSW 810', 'A-',
                                    'Rowland, J'],
                                   ['Jobs, S', '10103', 'CS 501', 'B',
                                    'Hawking, S'],
                                   ['Musk, E', '10183', 'SSW 555', 'A',
                                    'Rowland, J'],
                                   ['Musk, E', '10183', 'SSW 810', 'A',
                                    'Rowland, J']]

        gd_table: List[List[str, str, str, str,
                            str]] = [row for row in self.rt.
                                     _student_grades_table_db_summary
                                     (r"/Users/bansripatel/Desktop/ssw-810/"
                                      r"810_startup/810_startup.db")]
        self.assertEqual(table4, gd_table)


class CheckException(unittest.TestCase):
    """Testing Exceptions"""
    def test_exception(self) -> None:
        """Test cases to check exceptions"""
        self.path1: str = "/Users/bansripatel/Desktop/ssw-810"
        self.path2: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/810_startup.db")
        self.rt: Repository = Repository(self.path1, self.path2, False)
        self.path3: str = (r"/Users/bansripatel/Desktop/ssw-810/"
                           r"810_startup/Not_exists.db")
        with self.assertRaises(FileNotFoundError):
            Repository("Not_exists", False)
        with self.assertRaises(FileNotFoundError):
            self.rt._get_students(os.path.join("dir_path", "students1.txt"))
        with self.assertRaises(sqlite3.OperationalError):
            Repository(self.path1, self.path3)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
