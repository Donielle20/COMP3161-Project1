with open('insert.sql', 'w') as file:
    file.write('-- Group 11\n')
    file.write('-- 620126475\n')
    file.write('-- 620138478\n')
    file.write('-- 620109436\n')
    file.write('-- 620147266\n')
    file.write('-- 620141763\n\n')
    file.write('DROP DATABASE registry;\n\n')
    file.write('CREATE DATABASE registry;\n\n')
    file.write('USE registry;\n\n')
    file.write('CREATE TABLE students (\n\tstud_id INTEGER(5) PRIMARY KEY,\n\tfirst_name varchar(50),\n\tlast_name(50),\n\tstud_email varchar(30),\n\tstud_password varchar(30)\n);\n\n')

with open('Students.csv', 'r') as sfile:
    line = sfile.readline()

    print(line)