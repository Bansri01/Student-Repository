from flask import Flask, render_template
import sqlite3
from typing import Dict

app: Flask = Flask(__name__)
DB_FILE: str = "/Users/bansripatel/Desktop/ssw-810/HW12/810_startup.db"


@app.route("/completed")
def s_summary() -> str:
    try:
        db: sqlite3.Connection = sqlite3.connect(DB_FILE)
        query: str = """select s.name as Student, s.cwid, g.course,
                        g.grade, i.name as Instructor from students s join
                        grades g on s.cwid = g.StudentCWID join instructors
                        i on g.InstructorCWID = i.cwid order by s.name"""

    except sqlite3.OperationalError as e:
        print(e)
        raise sqlite3.OperationalError

    data: Dict[str, str] = [{"name": name, "cwid": cwid, "course": course,
                             "grade": grade, "instructor": instructor} for
                            name, cwid, course, grade, instructor in
                            db.execute(query)]

    db.close()

    return render_template("student_summary.html", title="Stevens Repository",
                           table_title="Student, Course, Grade and Instructor",
                           students=data)


app.run(debug=True)
