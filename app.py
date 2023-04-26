from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)

@app.route('/register/student', methods=['POST'])
def register_student():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        student_id = request.form.get('student_id')
        password = request.form.get('password')

        cursor.execute(f"INSERT INTO StudentUser (student_id, password) VALUES('{student_id}','{password}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Student User Added'}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)

@app.route('/register/lecturer', methods=['POST'])
def register_lecturer():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        lecturer_id = request.form.get('lecturer_id')
        password = request.form.get('password')

        cursor.execute(f"INSERT INTO LecturerUser (lecturer_id, password) VALUES('{lecturer_id}','{password}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Lecturer User Added'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 400)

@app.route('/register/admin', methods=['POST'])
def register_admin():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        adminID = request.form.get('adminID')
        password = request.form.get('password')

        cursor.execute(f"INSERT INTO AdminUser (adminID, password) VALUES('{adminID}','{password}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Admin User Added'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 400)

# @app.route('/register_user', methods=['POST'])
# def register_user():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        userID = request.form.get('userID')
        password = request.form.get('password')
        accountType = request.form.get('accountType')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        cursor.execute(f"INSERT INTO User VALUES('{userID}','{password}','{accountType}','{first_name}','{last_name}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'User Added'}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/student/login', methods=['POST'])
def  student_login():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        student_id = request.form.get('student_id')
        password = request.form.get('password')

        cursor.execute(f"SELECT * FROM StudentUser WHERE student_id='{student_id}' AND password='{password}'")
        result = cursor.fetchone()

        if result:
            cursor.close()

            cnx.close()

            return make_response({'SUCCESS': 'Login Successfull'}, 200)
                
        else:
            return make_response({'ERROR': 'User Credentials Incorrect or User Does Not Exist'}, 400)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)

@app.route('/lecturer/login', methods=['POST'])
def  lecturer_login():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        lecturer_id = request.form.get('lecturer_id')
        password = request.form.get('password')

        cursor.execute(f"SELECT * FROM LecturerUser WHERE lecturer_id='{lecturer_id}' AND password='{password}'")
        result = cursor.fetchone()

        if result:
            cursor.close()

            cnx.close()

            return make_response({'SUCCESS': 'Login Successfull'}, 200)
                
        else:
            return make_response({'ERROR': 'User Credentials Incorrect or User Does Not Exist'}, 400)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)

@app.route('/admin/login', methods=['POST'])
def  admin_login():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        adminID = request.form.get('adminID')
        password = request.form.get('password')

        cursor.execute(f"SELECT * FROM AdminUser WHERE adminID='{adminID}' AND password='{password}'")
        result = cursor.fetchone()

        if result:
            cursor.close()

            cnx.close()

            return make_response({'SUCCESS': 'Login Successfull'}, 200)
                
        else:
            return make_response({'ERROR': 'User Credentials Incorrect or User Does Not Exist'}, 400)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)

@app.route('/create_course', methods=['POST'])
def create_course():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        adminID = request.form.get('adminID')
        course_id = request.form.get('course_id')
        course_name = request.form.get('course_name')

        cursor.execute(f"SELECT adminID FROM AdminUser WHERE adminID='{adminID}'")
        result = cursor.fetchone()
        
        if result:
            cursor.execute(f"INSERT INTO courses VALUES('{course_id}', '{course_name}')")
            cursor.execute(f"INSERT INTO createcourse VALUES('{course_id}', '{adminID}')")
            
            cnx.commit()
            cursor.close()
            cnx.close()

            return make_response({'SUCCESS': "Course Added"}, 200)
        else:
            cursor.close()
            cnx.close()

            return make_response({'UNAUTHORIZED ACCESS': "Only Admins Can Create Courses"}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/retrieve/courses', methods=['GET'])
def get_customers():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        cursor.execute(f"SELECT * from courses")

        courses_list = []

        for course_id, course_name in cursor:
            courses = {}
            courses['course_id'] = course_id
            courses['course_name'] = course_name
            courses_list.append(courses)
        cursor.close()
        cnx.close()
        return make_response(courses_list, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)
    
@app.route('/retrieve/courses/<course_id>', methods=['GET'])
def get_courses(course_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        cursor.execute(f"SELECT * from courses WHERE course_id='{course_id}'")
        row = cursor.fetchone()

        # course = {}
        if row is not None:
            course_id, course_name = row
            course = {}
            course['course_id'] = course_id
            course['course_name'] = course_name

            cursor.close()
            cnx.close()
            return make_response(course, 200)
        else:
            return make_response({'error': 'Course not found'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)
    
@app.route('/retrieve/lectures/<lecturer_id>', methods=['GET'])
def get_courses_lecturer(lecturer_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        # cursor.execute(f"SELECT * from Teaches WHERE lecturer_id='{lecturer_id}'")
        cursor.execute(f"SELECT courses.course_name, courses.course_id FROM Teaches JOIN courses ON Teaches.course_id = courses.course_id WHERE Teaches.lecturer_id = {lecturer_id}")

        courses_list = []

        for lecturer_id, course_id in cursor:
            courses = {}
            courses['lecturer_id'] = lecturer_id
            courses['course_id'] = course_id
            courses_list.append(courses)
        cursor.close()
        cnx.close()
        return make_response(courses_list, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)
    
@app.route('/course/register/lecturer', methods=['POST'])
def register_lecturer_course():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        lecturer_id = request.form.get('lecturer_id')
        course_id = request.form.get('course_id')

        cursor.execute(f"INSERT INTO Teaches (lecturer_id, course_id) VALUES('{lecturer_id}','{course_id}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Lecturer was Added to a Course'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/course/register/student', methods=['POST'])
def register_student_course():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream') 
        
        cursor = cnx.cursor()

        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')

        cursor.execute(f"INSERT INTO Register (student_id, course_id) VALUES('{student_id}','{course_id}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Student was Added to a Course'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/create/calendar/events', methods=['POST'])
def create_calendar_events():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        course_id = request.form.get('course_id')
        lecturer_id = request.form.get('lecturer_id')
        eventName = request.form.get('eventName')
        eventDate = request.form.get('eventDate')

        cursor.execute(f"INSERT INTO CalendarEvents (course_id, lecturer_id, eventName, eventDate) VALUES('{course_id}','{lecturer_id}','{eventName}','{eventDate}')")

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'Calendar Event added to a Course'}, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/retrieve/courses/members/<course_id>', methods=['GET'])
def get_members(course_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        cursor.execute(f"SELECT Lecturer.lecturer_id, Lecturer.first_name, Lecturer.last_name, 'lecturer' AS member_type FROM Teaches INNER JOIN Lecturer ON Teaches.lecturer_id = Lecturer.lecturer_id WHERE Teaches.course_id = '{course_id}' UNION SELECT students.student_id, students.first_name, students.last_name, 'student' AS member_type FROM Register INNER JOIN students ON Register.student_id = students.student_id WHERE Register.course_id = '{course_id}'")

        members_list = []

        for lecturer_id,first_name, last_name, member_type in cursor:
            members = {}
            members['lecturer_id'] = lecturer_id
            members['first_name'] = first_name
            members['last_name'] = last_name
            members['member_type'] = member_type
            members_list.append(members)
        cursor.close()
        cnx.close()
        return make_response(members_list, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/retrieve/calendar/events/<course_id>', methods=['GET'])
def get_calendar_events(course_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        cursor.execute(f"SELECT * from CalendarEvents WHERE course_id = '{course_id}'")

        events_list = []

        for eventID, course_id, lecturer_id, eventName, eventDate in cursor:
            events = {}
            events['eventID'] = eventID
            events['course_id'] = course_id
            events['lecturer_id'] = lecturer_id
            events['eventName'] = eventName
            events['eventDate'] = eventDate
            events_list.append(events)
        cursor.close()
        cnx.close()
        return make_response(events_list, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/retrieve/calendar/events/<eventDate>/<student_id>', methods=['GET'])
def get_calendar_events_date(eventDate,student_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

        cursor = cnx.cursor()

        cursor.execute(f"SELECT ce.* FROM CalendarEvents ce INNER JOIN Register r ON ce.course_id = r.course_id WHERE r.student_id = {student_id} AND DATE(ce.eventDate) = '{eventDate}'")

        events_list = []

        for eventID, course_id, lecturer_id, eventName, eventDate in cursor:
            events = {}
            events['eventID'] = eventID
            events['course_id'] = course_id
            events['lecturer_id'] = lecturer_id
            events['eventName'] = eventName
            events['eventDate'] = eventDate
            events_list.append(events)
        cursor.close()
        cnx.close()
        return make_response(events_list, 200)
    except:
        return make_response({'error': 'An error has occured'}, 400)

# @app.route('/retrieve/members/<lecturerID>', methods=['GET'])
# def get_courses_lecturer(lecturerID):
#     try:
#         cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')

#         cursor = cnx.cursor()

#         cursor.execute(f"SELECT * from Teaches WHERE lecturerID='{lecturerID}'")

#         courses_list = []

#         for lecturerID, courseID in cursor:
#             courses = {}
#             courses['lecturerID'] = lecturerID
#             courses['courseID'] = courseID
#             courses_list.append(courses)
#         cursor.close()
#         cnx.close()
#         return make_response(courses_list, 200)
#     except:
#         return make_response({'error': 'An error has occured'}, 400)