start = 0
lst = []
count = 1

with open('Students.csv', 'r') as file:
    with open('Students_New.csv', 'a') as wfile:
        file.readline()
        for i in range(0,100000):
            line = file.readline().split(",")
            line[0] = count
            line.pop()

            separator = ","
            result = separator.join(map(str, line))
            print(result)
            wfile.write(result + ",\n")
            count+=1