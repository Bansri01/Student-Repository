"""Author: Bansri Patel
   Created: 4/10/2021

   Purpose:
   To test the Student and instructor class from HW09
"""

import unittest
import os
from typing import Iterator, Tuple, Dict, List
from HW09_Bansrikumari_Patel import Student, Instructor, Repository


class TestStudent(unittest.TestCase):
    """Testing Student class"""
    def test_student(self) -> None:
        """test cases to test Student class"""
        self.path: str = "/Users/bansripatel/Desktop/ssw-810"
        self.rt: Repository = Repository(self.path, False)
        table1: Dict[str: [str, str, List[str]]] = {cwid: student.st_data()
                                                    for cwid, student in
                                                    self.rt._students_dict.
                                                    items()
                                                    }
        st_table: Dict[str: [str, str, List[str]]] = {'10103':
                                                      ['10103', 'Baldwin, C',
                                                       ['CS 501', 'SSW 564',
                                                        'SSW 567', 'SSW 687']],
                                                      '10115':
                                                      ['10115', 'Wyatt, X',
                                                       ['CS 545', 'SSW 564',
                                                        'SSW 567', 'SSW 687']],
                                                      '10172':
                                                      ['10172', 'Forbes, I',
                                                       ['SSW 555', 'SSW 567']],
                                                      '10175':
                                                      ['10175', 'Erickson, D',
                                                       ['SSW 564', 'SSW 567',
                                                        'SSW 687']],
                                                      '10183':
                                                      ['10183', 'Chapman, O',
                                                       ['SSW 689']],
                                                      '11399':
                                                      ['11399', 'Cordova, I',
                                                       ['SSW 540']],
                                                      '11461':
                                                      ['11461', 'Wright, U',
                                                       ['SYS 611', 'SYS 750',
                                                        'SYS 800']],
                                                      '11658':
                                                      ['11658', 'Kelly, P',
                                                       ['SSW 540']],
                                                      '11714':
                                                      ['11714', 'Morton, A',
                                                       ['SYS 611', 'SYS 645']],
                                                      '11788':
                                                      ['11788', 'Fuller, E',
                                                       ['SSW 540']]}

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
