import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    ###  no ; needed 
    ### the WHERE is preceded by ?; when the code is executed, we write our values
    ### think of ? as a place holder ie %s
    ###  DB. execute is a tuple...i believe the query comes from WHERE github =?

    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()  ### gets a row; places values via columns in a TUPLE. 
    return row

def connect_to_db():
    #### this code is used to interact wit hthe databse so the queries can be executed.
    global DB, CONN  #
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()  #go to the beginning of db  ## different from CONN.commit()

def make_new_student(first_name, last_name, github):

    ###INSERT into projectName values.... when we want to add things to your project
    query = """ INSERT into Students values (?,?,?)"""

    #below: DB.execute built in to sql; query is a variable(above) and the ? are the parameters of concern
    DB.execute(query, (first_name, last_name, github)) #our fn parameter, query ?, db.execute command ALL MATCH!  
                            #parameters above are TUPLES
    CONN.commit() #save this data forever, and commit it to db connection, and NOT THE CURSOR
    return "Successfully added student: %s %s" %(first_name, last_name)


def project_query(title):
    """ Query our database projects table and pass in the project title then print the project id, description 
        and max grade"""

    query = """SELECT * FROM projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()  ### gets a row; places values via columns in a TUPLE. 
    return "Project Data: %s %s %s %s"%(row[0], row[1], row[2], row[3])

def get_grade(project_title, first_name, last_name):
    """ Query our database grades join students tables with the project title, the student first_name and the last name then print grade"""

    query = """SELECT grades.grade FROM grades JOIN students ON (grades.student_github = students.github) WHERE grades.project_title  = ? AND
    students.first_name = ? AND students.last_name = ?"""
    DB.execute(query, (project_title, first_name, last_name,))
    row = DB.fetchone()  ### gets a row; places values via columns in a TUPLE. 
    return row[0]


def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ") #python doesn't continue the while loop until user puts something in
        tokens = input_string.split() #tokens = list of strings [" " 
        command = tokens[0] #get first item from the list
        args = tokens[1:] #args gets everything from 2nd thing in the list to the end

        if command == "student": #if the first thing in the list is student 
            get_student_by_github(*args)  #call this fn and bring the rest of arg [1:]
        elif command == "new_student": #if our first thing in the list is new_student
            make_new_student(*args)  #call this fn and bring the rest of args to it
        elif command == "project": #call function to retrieve project data
            project_query(*args)
        elif command == "get_grade":
            get_grade(*args)

    CONN.close()  # close db

if __name__ == "__main__":
    main()
