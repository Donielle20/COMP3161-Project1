with open('courses.sql', 'w') as file:
    file.write('-- Group 11\n')
    file.write('-- 620126475\n')
    file.write('-- 620138478\n')
    file.write('-- 620109436\n')
    file.write('-- 620147266\n')
    file.write('-- 620141763\n\n')
    file.write('DROP DATABASE edustream;\n\n')
    file.write('CREATE DATABASE edustream;\n\n')
    file.write('USE edustream;\n\n')
    file.write('CREATE TABLE students (\n\tcourse_id varchar(10) PRIMARY KEY,\n\tcourse_name varchar(50)\n);\n\n')

    course_num = 1000
    start = "COMP"
    name = "Computer Science "

    file.write('INSERT INTO students (course_id,course_name) VALUES\n')

    for i in range(0,200):
        course_num = course_num + 5
        new_num = start + str(course_num)
        # print(start + str(course_num))
        file.write('('+ "'" + new_num + "'" + ',' + "'" + name + str(i) + "'" + '),\n')