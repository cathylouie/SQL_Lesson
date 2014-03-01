from flask import Flask, render_template, request, abort
import hackbright_app

app = Flask(__name__)

@app.route("/project_title")
def get_project_title():
    hackbright_app.connect_to_db()
    projects = hackbright_app.get_all_projects()
    return render_template("all_projects.html", projects=projects)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/new_student")
def make_new_student():
    return render_template("make_new_student.html")

@app.route("/new_project")
def add_new_project():
    return render_template("add_new_project.html")

@app.route("/new_grade")
def add_new_grade():
    hackbright_app.connect_to_db()
    projects = hackbright_app.get_all_projects()
    return render_template("all_projects_for_grade.html", projects=projects)

@app.route("/project/<id>/")
def get_student_and_grade_from_project(id):
    hackbright_app.connect_to_db()
    title = hackbright_app.get_project_title(id)
    if title is None:
        abort(404)
    #print title
    list_of_grades = hackbright_app.get_grade_by_title(title)
    html = render_template("project_info.html", list_of_grades=list_of_grades)
    return html


@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    list_of_grades = hackbright_app.get_grade_by_github(student_github)
    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2],
                                                list_of_grades=list_of_grades)
    return html

@app.route("/new_student/info/")
def new_student_info():
    hackbright_app.connect_to_db()
    new_student_first_name = request.args.get("first_name")
    new_student_last_name = request.args.get("last_name")
    new_student_github = request.args.get("github")
    hackbright_app.make_new_student(new_student_first_name, new_student_last_name, new_student_github)
    html = render_template("completed_new_student.html",first_name=new_student_first_name,
                                                        last_name=new_student_last_name,
                                                        github=new_student_github)

    return html

@app.route("/new_project/info/")
def new_project_info():
    hackbright_app.connect_to_db()
    new_project_title = request.args.get("title")
    new_project_description = request.args.get("description")
    new_project_max_grade = request.args.get("max_grade")
    hackbright_app.add_new_project(new_project_title, new_project_description, new_project_max_grade)
    html = render_template("completed_new_project.html",title=new_project_title,
                                                        description=new_project_description,
                                                        max_grade=new_project_max_grade)

    return html

@app.route("/new_grade/info/<id>")
def new_grade_info(id):
    hackbright_app.connect_to_db()
    title = hackbright_app.get_project_title(id)
    list_of_grades = hackbright_app.get_grade_by_title(title)
    html = render_template("grade_input.html", list_of_grades=list_of_grades,
                                               id=id)

    return html

@app.route("/completed_new_grade/info/<id>")
def completed_new_grade(id):
    hackbright_app.connect_to_db()
    new_grade = request.args.get("grade")
    title = hackbright_app.get_project_title(id)
    list_of_grades = hackbright_app.get_grade_by_title(title)
    row = hackbright_app.change_a_grade(title,new_grade)
    print row
    html = render_template("completed_new_grade.html", github=list_of_grades[0][2],
                                                       project_title=title,
                                                       grade=new_grade)
    return html

if __name__ == "__main__":
    app.run(debug=True)