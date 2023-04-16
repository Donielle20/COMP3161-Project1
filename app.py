from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)

@app.route('/register_user', methods=['POST'])
def register_user():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        userID = request.form.get('userID')
        password = request.form.get('password')
        accountType = request.form.get('accountType')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        cursor.execute(f"INSERT INTO User VALUES('{userID}','{password}','{accountType}','{first_name}','{last_name}')")
        # cursor.execute(f"SELECT * FROM students")
        # result = cursor.fetchall()

        cnx.commit()

        cursor.close()

        cnx.close()

        return make_response({'SUCCESS': 'User Added'}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/user_login', methods=['GET'])
def  user_login():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        userID = request.form.get('userID')
        password = request.form.get('password')

        cursor.execute(f"SELECT * FROM User WHERE userID='{userID}' AND password='{password}'")
        result = cursor.fetchone()

        if result:
            cursor.close()

            cnx.close()

            return make_response({'SUCCESS': 'Login Successfull'}, 200)
                
        else:
            return make_response({'ERROR': 'User Credentials Incorrect'}, 400)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)
    
@app.route('/create_course', methods=['POST'])
def create_course():
    try:
        cnx = mysql.connector.connect(user='root', password='Vanvillabom16', host='127.0.0.1', database='edustream')
        
        cursor = cnx.cursor()

        userID = request.form.get('userID')
        password = request.form.get('password')
        course_id = request.form.get('course_id')
        course_name = request.form.get('course_name')

        cursor.execute(f"SELECT * FROM User WHERE userID='{userID}' AND password='{password}'")
        result = cursor.fetchone()
        userID, password, accountType = result
        cursor.close()
        cnx.close()
        if (accountType == "admin"):
            return make_response({'SUCCESS': accountType}, 200)
        else:
            return make_response({'UNAUTHORIZED ACCESS': "Only Admins Can Create Courses"}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 400)