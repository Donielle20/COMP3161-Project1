with open('Students.csv', 'w') as file:
    file.write('stud_id,first_name,last_name,stud_email,stud_password\n')

passwords = []

with open('trial.txt', 'r') as tfile:
    
    tline = tfile.readline()
    tline = tline.strip()
    passwords.append(tline)

    while tline:
        tline = tfile.readline()
        tline = tline.strip()
        passwords.append(tline)
# print(passwords)

with open('ExportCSV.csv', 'r') as efile:

    line = efile.readline()

    count = 0

    while line:
        with open('Students.csv', 'a') as file:

            line = efile.readline()
            line = line.strip()
            file.write(line + passwords[count] +"\n")
            count+=1
