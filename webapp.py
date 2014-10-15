from flask import Flask, render_template, request
import hackbright_app
app = Flask(__name__)

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")

    row1 = hackbright_app.get_student_by_github(student_github)
    row2 = hackbright_app.get_grade("Pyglet", "Snoopy", "dog")
    print row2

    html = render_template("student_info.html", first_name = row1[0], 
        last_name = row1[1], github = row1[2], grade=row2)




    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")


if __name__ == "__main__":
    app.run(debug=True)