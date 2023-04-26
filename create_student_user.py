count = 0
with open('student_user.sql', 'w') as wfile:
    wfile.write(f"INSERT INTO StudentUser (student_id, password) VALUES\n")
with open('Students_New.csv', 'r') as sfile:
    with open('passwords.txt', 'r') as pfile:
        for line in sfile:
            if count == 0:
                count+=1
                continue
            read = line.split(",")
            sub = pfile.readline()
            count+=1
            if (count == 100000):
                print(read[0],sub)
                with open('student_user.sql', 'a') as wfile:
                    wfile.write(f"({int(read[0])},'{sub.strip()}'),\n")
                    break
            with open('student_user.sql', 'a') as wfile:
                wfile.write(f"({int(read[0])},'{sub.strip()}'),\n")

# with open('passwords.txt', 'r') as pfile:
#     lines = pfile.readlines()
#     print(lines)