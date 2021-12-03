import sys

inputs = list(sys.argv[2].split(","))

students = open(sys.argv[1], mode = "r", encoding="utf-8")
students = list(students.read().split("\n"))

student_dict = {student.split(":")[0]:student.split(":")[1] for student in students}

for name in inputs:
    try:
        print("Name: {name}, Univesity:".format(name = name), student_dict[name], end=" ")
    except:
        print("No record of '{name}' was found!".format(name = name), end=" ")