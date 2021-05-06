"""Author: Bansri Patel
   Created: 4/3/2021

   Purpose:
   To implement Date Arithmetic Operations, field separated file reader and
   File Analyzer.
"""
import os
from datetime import datetime, timedelta
from typing import Tuple, List, Iterator
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """To find date after 2/27/2020 and 2/27/2019 and to find number of days
       between 2/1/2019 and 9/30/2019
    """
    dt1: datetime = datetime.strptime("sep 30 2019", "%b %d %Y")
    dt2: datetime = datetime.strptime("feb 1 2019", "%b %d %Y")
    three_days_after_02272020: datetime = \
        datetime.strptime("feb 27 2020", "%b %d %Y") + timedelta(days=3)
    three_days_after_02272019: datetime = \
        datetime.strptime("feb 27 2019", "%b %d %Y") + timedelta(days=3)
    days_passed_02012019_09302019: int = (dt1 - dt2).days

    return three_days_after_02272020, three_days_after_02272019,\
        days_passed_02012019_09302019


def file_reader(path: str, fields: int, sep: str = ",", header: bool = False)\
     -> Iterator[List[str]]:
    """To read field-separated text files and yield a tuple with all of
       the values from a single line in the file
    """
    try:
        fp: IO = open(path, "r")
        with fp as f:
            if header:
                next(f)
            for line in f:
                s_list: List(str) = line.strip("\n").split(sep)
                f_count: int = len(s_list)
                if f_count != fields:
                    raise ValueError(f"{path} has {f_count} fields on \
                                     line {line} but expected {fields}")
                yield tuple(s_list)
    except FileNotFoundError:
        raise FileNotFoundError("File not found at this path")


class FileAnalyzer:
    """To analyze the python files"""
    def __init__(self, directory: str) -> None:
        """init method to initialize the attributes"""
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory:{directory} not found")
        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """Count and return the number of classes, functions, lines and
           characters in a python file
        """
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                try:
                    fp: IO = open(os.path.join(self.directory, file), "r")
                except FileNotFoundError:
                    print(f"File {fp} not found on this path")
                with fp:
                    class_ct: int = 0
                    function_ct: int = 0
                    line_ct: int = 0
                    char_ct: int = 0

                    for line in fp:
                        if line.strip().startswith("class "):
                            class_ct += 1
                        elif line.strip().startswith("def "):
                            function_ct += 1

                        line_ct += 1
                        char_ct += len(line)

                    self.files_summary[str(os.path.join(self.directory,
                                       file))] = {"class": class_ct,
                                                  "function": function_ct,
                                                  "line": line_ct,
                                                  "char": char_ct}

    def pretty_print(self) -> None:
        """Use of Prettytable to format the table"""
        p_table: PrettyTable = PrettyTable(field_names=["File Name", "Classes",
                                                        "Functions", "Lines",
                                                        "Characters"])
        for key, value in self.files_summary.items():
            p_table.add_row([key] + list(value.values()))

        return p_table


def main() -> None:
    """call methods date_arithmetic, file_reader and methods in FileAnalyzer"""
    print("Date Arithmentic Operations..")
    print(date_arithmetic())
    print("\n")

    print("field seperated file reader..")
    path: str = "/Users/bansripatel/Desktop/ssw-810/student_majors.txt"
    for cwid, name, major in file_reader(path, 3, sep='|', header=True):
        print(f"cwid: {cwid} name: {name} major: {major}")
    print("\n")

    print("Scanning directories and files..")
    path: str = "/Users/bansripatel/Desktop/ssw-810"
    obj: FileAnalyzer = FileAnalyzer(path)
    print(obj.pretty_print())


if __name__ == "__main__":
    main()
