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

@app.route("/project/<id>/")
def get_student_and_grade_from_project(id):
    hackbright_app.connect_to_db()
    title = hackbright_app.get_project_title(id)
    if title is None:
        abort(404)
    print title
    list_of_grades = hackbright_app.get_grade_by_title(title)
    html = render_template("project_info.html", list_of_grades=list_of_grades)
    print list_of_grades
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

if __name__ == "__main__":
    app.run(debug=True)