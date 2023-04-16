with open('insert.sql', 'w') as file:
    file.write('-- Group 11\n')
    file.write('-- 620126475\n')
    file.write('-- 620138478\n')
    file.write('-- 620109436\n')
    file.write('-- 620147266\n')
    file.write('-- 620141763\n\n')
    file.write('DROP DATABASE edustream;\n\n')
    file.write('CREATE DATABASE edustream;\n\n')
    file.write('USE edustream;\n\n')
    file.write('CREATE TABLE students (\n\tstudent_id INTEGER(5) PRIMARY KEY,\n\tfirst_name varchar(50),\n\tlast_name(50),\n\temail varchar(30)\n);\n\n')

with open('Students.csv', 'r') as sfile:
    line = sfile.readline()
    line2 = sfile.readlines()

    with open('insert.sql', 'a') as file2:
        file2.write('INSERT INTO students (student_id,first_name,last_name,email) VALUES\n')

        for element, i in enumerate(line2[1:]):
                new_list = []
                new_line = []
                new_line = i.split(",")
                new_line[-1] = new_line[-1].strip()
                del new_line[-1]
                # print(new_line)

                for i in new_line:
                    if i.isdigit():
                        new_list.append(int(i))
                    else:
                        new_list.append(i)
                    # print(new_list)

                separator = ', '
                new_list = separator.join([f"'{value}'" if isinstance(value, str) else str(value) for value in new_list])

                # print(new_list)
                if element == len(line2[1:]) - 1:
                    file2.write("(" + new_list + ");\n")
                else:
                    file2.write("(" + new_list + "),\n")
        
    # print(new_list)
    