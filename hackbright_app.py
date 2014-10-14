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
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

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
    print "Successfully added student: %s %s" %(first_name, last_name)


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

    CONN.close()  # close db

if __name__ == "__main__":
    main()
