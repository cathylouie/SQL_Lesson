import sqlite3

DB = None
CONN = None

def get_grade_by_title(project_title):

# Do some joining to make a VIEW called GradesView so to connect student's grade with student's name via student's github name,
# then SELECT Students.first_name and students.last_name, Grades.grade WHERE Grades.project_title = raw_input.
    #query = """ SELECT Students.first_name, Students.last_name, Grades.project_title, Grades.grade FROM Students INNER JOIN Grades ON (Students.github=Grades.student_github)"""


    
    DB.execute(query, (Grades.project_title,))
    row = DB.fetchone()
    print """\
Title: %s 
Student: %s %s
Grade: %s"""%(row[0], row[1], row[2], row[4])

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Title: %s 
Description: %s
Maximum grade: %s"""%(row[0], row[1], row[2])   

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            get_project_by_title(*args)
    #    elif command == "new_project":
    #        add_new_project(*args)

#def add_new_project(title, description, max_grade): """Couldn't figure out how to INSERT the autoincrement id and a sentence for the'description' field
#    query = """INSERT into Projects values (?,?,?)"""
#    DB.execute(query, (title, description, max_grade))

#    CONN.commit()
#   print "Successfully added project:%s %s %s"%(title, description, max_grade)

#    CONN.close()          

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name,last_name,github))

    CONN.commit()
    print "Successfully added student: %s %s"%(first_name,last_name)

    CONN.close()

if __name__ == "__main__":
    main()
