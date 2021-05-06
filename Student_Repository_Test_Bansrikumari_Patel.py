"""Author: Bansri Patel
   Created: 4/10/2021
   Updated: 4/19/2021

   Purpose:
   To test the Major, Student and instructor class
"""

import unittest
import os
from typing import Iterator, Tuple, Dict, List
from HW10_Bansrikumari_Patel import Student, Instructor, Repository


class TestMajor(unittest.TestCase):
    """Testing Major class"""
    def test_major(self) -> None:
        """test cases to test Major class"""
        self.path: str = "/Users/bansripatel/Desktop/ssw-810"
        self.rt: Repository = Repository(self.path, False)
        table3: List[Tuple(str, List[str], List[str])] = [majors.major_data()
                                                          for majors in self.
                                                          rt._majors_dict.
                                                          values()
                                                          ]
        m_table: List[Tuple(str, List[str],
                      List[str])] = [('SFEN', ['SSW 540', 'SSW 555', 'SSW 564',
                                      'SSW 567'], ['CS 501', 'CS 513',
                                      'CS 545']), ('SYEN', ['SYS 612',
                                                   'SYS 671', 'SYS 800'],
                                                   ['SSW 540', 'SSW 565',
                                                    'SSW 810'])]
        self.assertEqual(m_table, table3)


class TestStudent(unittest.TestCase):
    """Testing Student class"""
    def test_student(self) -> None:
        """test cases to test Student class"""
        self.path: str = "/Users/bansripatel/Desktop/ssw-810"
        self.rt: Repository = Repository(self.path, False)
        table1: List[List[str, str, str, List[str],
                     List[str], List[str], float]] = [student.st_data() for
                                                      cwid, student in self.rt.
                                                      _students_dict.items()]
        st_table: List[List[str, str, str, List[str],
                       List[str], List[str], float]] = [['10103', 'Baldwin, C',
                                                         'SFEN', ['CS 501',
                                                                  'SSW 564',
                                                                  'SSW 567',
                                                                  'SSW 687'], [
                                                                  'SSW 540',
                                                                  'SSW 555'],
                                                         [], 3.44],
                                                        ['10115', 'Wyatt, X',
                                                        'SFEN', ['CS 545',
                                                         'SSW 564', 'SSW 567',
                                                                 'SSW 687'],
                                                         ['SSW 540',
                                                          'SSW 555'], [], 3.81
                                                         ],
                                                        ['10172', 'Forbes, I',
                                                        'SFEN', ['SSW 555',
                                                         'SSW 567'],
                                                         ['SSW 540',
                                                         'SSW 564'], ['CS 501',
                                                         'CS 513', 'CS 545'
                                                                      ], 3.88],
                                                        ['10175',
                                                        'Erickson, D', 'SFEN',
                                                         ['SSW 564', 'SSW 567',
                                                          'SSW 687'],
                                                         ['SSW 540',
                                                          'SSW 555'],
                                                         ['CS 501', 'CS 513',
                                                          'CS 545'], 3.58],
                                                        ['10183', 'Chapman, O',
                                                         'SFEN', ['SSW 689'],
                                                         ['SSW 540', 'SSW 555',
                                                          'SSW 564',
                                                          'SSW 567'],
                                                         ['CS 501', 'CS 513',
                                                          'CS 545'], 4.0],
                                                        ['11399', 'Cordova, I',
                                                         'SYEN', ['SSW 540'],
                                                         ['SYS 612', 'SYS 671',
                                                          'SYS 800'], [], 3.0],
                                                        ['11461', 'Wright, U',
                                                         'SYEN', ['SYS 611',
                                                                  'SYS 750',
                                                                  'SYS 800'],
                                                         ['SYS 612',
                                                          'SYS 671'],
                                                         ['SSW 540', 'SSW 565',
                                                          'SSW 810'], 3.92],
                                                        ['11658', 'Kelly, P',
                                                         'SYEN', [],
                                                         ['SYS 612', 'SYS 671',
                                                          'SYS 800'],
                                                         ['SSW 540',
                                                          'SSW 565',
                                                          'SSW 810'], 0.0],
                                                        ['11714', 'Morton, A',
                                                         'SYEN', ['SYS 611',
                                                                  'SYS 645'],
                                                         ['SYS 612', 'SYS 671',
                                                          'SYS 800'],
                                                         ['SSW 540', 'SSW 565',
                                                          'SSW 810'], 3.0],
                                                        ['11788', 'Fuller, E',
                                                         'SYEN', ['SSW 540'],
                                                         ['SYS 612', 'SYS 671',
                                                          'SYS 800'], [], 4.0]]

        self.assertEqual(st_table, table1)


class TestInstructor(unittest.TestCase):
    """Testing Instructor class"""
    def test_instructor(self) -> None:
        """Test cases to test Instructor class"""
        self.path: str = "/Users/bansripatel/Desktop/ssw-810"
        self.rt: Repository = Repository(self.path, False)
        table2: set[Tuple[str, str, str, str, int]] = {tuple(inst_t) for
                                                       instructor in
                                                       self.rt.
                                                       _instructors_dict.
                                                       values() for inst_t
                                                       in instructor.
                                                       inst_data()}
        inst_table: set[Tuple[str, str, str, str, int]] = {('98765',
                                                            'Einstein, A',
                                                            'SFEN', 'SSW 567',
                                                            4),
                                                           ('98765',
                                                            'Einstein, A',
                                                            'SFEN', 'SSW 540',
                                                            3),
                                                           ('98764',
                                                            'Feynman, R',
                                                            'SFEN', 'SSW 564',
                                                            3),
                                                           ('98764',
                                                            'Feynman, R',
                                                            'SFEN', 'SSW 687',
                                                            3),
                                                           ('98764',
                                                            'Feynman, R',
                                                            'SFEN', 'CS 501',
                                                            1),
                                                           ('98764',
                                                            'Feynman, R',
                                                            'SFEN', 'CS 545',
                                                            1),
                                                           ('98763',
                                                            'Newton, I',
                                                            'SFEN', 'SSW 555',
                                                            1),
                                                           ('98763',
                                                            'Newton, I',
                                                            'SFEN', 'SSW 689',
                                                            1),
                                                           ('98760',
                                                            'Darwin, C',
                                                            'SYEN', 'SYS 800',
                                                            1),
                                                           ('98760',
                                                            'Darwin, C',
                                                            'SYEN', 'SYS 750',
                                                            1),
                                                           ('98760',
                                                            'Darwin, C',
                                                            'SYEN', 'SYS 611',
                                                            2),
                                                           ('98760',
                                                            'Darwin, C',
                                                            'SYEN', 'SYS 645',
                                                            1)}

        self.assertEqual(inst_table, table2)


class CheckException(unittest.TestCase):
    """Testing Exceptions"""
    def test_exception(self) -> None:
        """Test cases to check exceptions"""
        self.path: str = "/Users/bansripatel/Desktop/ssw-810"
        self.rt: Repository = Repository(self.path, False)
        with self.assertRaises(FileNotFoundError):
            Repository("Not_exists", False)
        with self.assertRaises(FileNotFoundError):
            self.rt._get_students(os.path.join("dir_path", "students1.txt"))


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
