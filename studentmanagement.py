def file():
    outfile = open("data.txt", 'a')
    print("Enter Student Details:")
    name = input("Enter name:")
    dept = input("Enter department:")
    mrks = input("Enter marks:")
    grade = ()
    if type(mrks) == type(2):
        print("Invalid Input!")
    int(mrks)
    if mrks >= 80:
        grade = "A"
    elif mrks >= 70:
        grade = "B"
    elif mrks >= 60:
        grade = "C"
    elif mrks >= 50:
        grade = "D"
    elif mrks >= 40:
        grade = "E"
    elif mrks < 40:
        grade = "Failed"

    outfile.write("name: " + name + "\n")
    outfile.write("department: " + dept + "\n")
    outfile.write("marks: " + int(int(mrks)) + "\n")
    outfile.write("grades: " + grade + "\n")

    outfile.close()
file()
