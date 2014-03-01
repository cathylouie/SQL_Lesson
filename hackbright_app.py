import sqlite3

DB = None
CONN = None

def get_all_projects():
    query = """SELECT id, title FROM Projects"""
    DB.execute(query, ())
    row = DB.fetchall()
    return row

def get_project_title(id):
    query = """SELECT title FROM Projects WHERE id = ?"""
    DB.execute(query,(id))
    try:
        row = DB.fetchone()
        return row[0]
    except:
        return None

def get_all_students(id):
    query = """SELECT title FROM Projects WHERE id = ?"""
    DB.execute(query,(id))
    try:
        row = DB.fetchone()
        return row[0]
    except:
        return None

def get_grade_by_title(project_title):
    query = """SELECT first_name, last_name, student_github, project_title, grade FROM Grades JOIN Students ON github=student_github WHERE project_title = ?""" 
    DB.execute(query, (project_title,))
    row = DB.fetchall()
    return row
    # print """\
    # Student: %s %s
    # Project Title: %s
    # Grade: %s"""%(row[0], row[1], row[2], row[3])

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
    Title: %s 
    Description: %s2
    Maximum grade: %s"""%(row[0], row[1], row[2])   

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row


def get_grade_by_github(grade):
    query = """SELECT first_name, last_name, project_title, grade FROM Students JOIN Grades ON github=student_github WHERE github = ?""" 
    DB.execute(query, (grade,))
    row = DB.fetchall()
    return row
    # Student: %s %s
    # Project: %s
    # Grade: %s"""%(index[0], index[1], index[2], index[3])

def make_new_student(first_name, last_name, github):
    print first_name, last_name, github
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name,last_name,github))
    CONN.commit()
    return "Successfully added student: %s %s %s"%(first_name,last_name, github)

def add_new_project(title, description, max_grade): 
    query = """INSERT into Projects (title, description, max_grade) values (?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project:%s %s %s"%(title, description, max_grade) 

def add_a_grade(student_github, project_title, grade): 
    query = """INSERT into Grades (student_github, project_title, grade) values (?,?,?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    return "Successfully added grade:%s %s %s"%(student_github, project_title, grade) 

def change_a_grade(title, grade): 
    query = """UPDATE Grades SET grade = ? WHERE project_title = ?"""
    DB.execute(query, (title, grade))
    CONN.commit()
    return "Successfully changed grade:%s"%(grade)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split(None,1)
        command = tokens[0]
        arguments = tokens[1]
        arguments1 = arguments.split(",")
        args = [x.strip() for x in arguments1]
        print args

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            get_project_by_title(*args)
        elif command == "new_project":
            add_new_project(*args)  
        elif command == "project_title":
            get_grade_by_title(*args)    
        elif command == "new_grade":
            add_a_grade(*args) 
        elif command == "show_all_grades":
            get_grade_by_student(*args)


    CONN.close()

if __name__ == "__main__":
    main()
