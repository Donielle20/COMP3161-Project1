
course_id = ['COMP1005', 'COMP1010', 'COMP1015', 'COMP1020', 'COMP1025', 'COMP1030', 'COMP1035', 'COMP1040', 'COMP1045', 'COMP1050', 'COMP1055', 'COMP1060', 'COMP1065', 'COMP1070', 'COMP1075', 'COMP1080', 'COMP1085', 'COMP1090', 'COMP1095', 'COMP1100', 'COMP1105', 'COMP1110', 'COMP1115', 'COMP1120', 'COMP1125', 'COMP1130', 'COMP1135', 'COMP1140', 'COMP1145', 'COMP1150', 'COMP1155', 'COMP1160', 'COMP1165', 'COMP1170', 'COMP1175', 'COMP1180', 'COMP1185', 'COMP1190', 'COMP1195', 'COMP1200', 'COMP1205', 'COMP1210', 'COMP1215', 'COMP1220', 'COMP1225', 'COMP1230', 'COMP1235', 'COMP1240', 'COMP1245', 'COMP1250', 'COMP1255', 'COMP1260', 'COMP1265', 'COMP1270', 'COMP1275', 'COMP1280', 'COMP1285', 'COMP1290', 'COMP1295', 'COMP1300', 'COMP1305', 'COMP1310', 'COMP1315', 'COMP1320', 'COMP1325', 'COMP1330', 'COMP1335', 'COMP1340', 'COMP1345', 'COMP1350', 'COMP1355', 'COMP1360', 'COMP1365', 'COMP1370', 'COMP1375', 'COMP1380', 'COMP1385', 'COMP1390', 'COMP1395', 'COMP1400', 'COMP1405', 'COMP1410', 'COMP1415', 'COMP1420', 'COMP1425', 'COMP1430', 'COMP1435', 'COMP1440', 'COMP1445', 'COMP1450', 'COMP1455', 'COMP1460', 'COMP1465', 'COMP1470', 'COMP1475', 'COMP1480', 'COMP1485', 'COMP1490', 'COMP1495', 'COMP1500', 'COMP1505', 'COMP1510', 'COMP1515', 'COMP1520', 'COMP1525', 'COMP1530', 'COMP1535', 'COMP1540', 'COMP1545', 'COMP1550', 'COMP1555', 'COMP1560', 'COMP1565', 'COMP1570', 'COMP1575', 'COMP1580', 'COMP1585', 'COMP1590', 'COMP1595', 'COMP1600', 'COMP1605', 'COMP1610', 'COMP1615', 'COMP1620', 'COMP1625', 'COMP1630', 'COMP1635', 'COMP1640', 'COMP1645', 'COMP1650', 'COMP1655', 'COMP1660', 'COMP1665', 'COMP1670', 'COMP1675', 'COMP1680', 'COMP1685', 'COMP1690', 'COMP1695', 'COMP1700', 'COMP1705', 'COMP1710', 'COMP1715', 'COMP1720', 'COMP1725', 'COMP1730', 'COMP1735', 'COMP1740', 'COMP1745', 'COMP1750', 'COMP1755', 'COMP1760', 'COMP1765', 'COMP1770', 'COMP1775', 'COMP1780', 'COMP1785', 'COMP1790', 'COMP1795', 'COMP1800', 'COMP1805', 'COMP1810', 'COMP1815', 'COMP1820', 'COMP1825', 'COMP1830', 'COMP1835', 'COMP1840', 'COMP1845', 'COMP1850', 'COMP1855', 'COMP1860', 'COMP1865', 'COMP1870', 'COMP1875', 'COMP1880', 'COMP1885', 'COMP1890', 'COMP1895', 'COMP1900', 'COMP1905', 'COMP1910', 'COMP1915', 'COMP1920', 'COMP1925', 'COMP1930', 'COMP1935', 'COMP1940', 'COMP1945', 'COMP1950', 'COMP1955', 'COMP1960', 'COMP1965', 'COMP1970', 'COMP1975', 'COMP1980', 'COMP1985', 'COMP1990', 'COMP1995', 'COMP2000']
import random
with open('Students_enrol.sql', 'w') as file:
    file.write(f"INSERT INTO Register(student_id, course_id) VALUES\n")
MAX_COURSES = 6
MIN_COURSES = 3
MIN_MEMBERS = 9

def generate_courses():
    return random.sample(course_id, k=random.randint(MIN_COURSES, MAX_COURSES))

def generate_students(num_students):
    students = []
    for student_id in range(1, num_students + 1):
        courses = generate_courses()
        while len(courses) < MIN_COURSES:
            courses = generate_courses()
        for course in courses:
            if len(course_roster[course]) < MIN_MEMBERS:
                courses.remove(course)
                break
        if len(courses) > MAX_COURSES:
            courses = courses[:MAX_COURSES]
        students.append({'student_id': student_id, 'courses': courses})
        for course in courses:
            course_roster[course].append(student_id)
    return students

course_roster = {}
for course in course_id:
    course_roster[course] = []

students = generate_students(100000)
with open('Students_enrol.sql', 'a') as file:
    for student in students:
        student_id = student['student_id']
        for course_id in student['courses']:
            file.write(f"({student_id}, '{course_id}'),\n")



# id = 1
# count = 1
# for i in range(1, 201):
#     course = f'COMP{i:04}'
#     print("(" + str(id) + "," + "'" + course + "'" + "),")
#     count += 1
#     if count == 6:
#         id += 1
#         count = 1

# id = 1
# count = 1
# for i in range(1005, 2001, 5):
#     course = f'COMP{i:04}'
#     print("(" + str(id) + "," + "'" + course + "'" + "),")
#     count += 1
#     if count == 6:
#         id += 1
#         count = 1
