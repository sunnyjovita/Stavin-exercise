# print("-----MENU-----")
# print("1. roti")
# print("2. nasi goreng")
# print("3. kentang goreng")
# choose = str(input("choose the number :"))
#
# if(choose=="1"):
#     print("7 ribu")
# elif(choose=="2"):
#     print("5 ribu")
# elif(choose=="3"):
#     print("6 ribu")
# else:
#     print("thankyou")

# def list():
#     print("student names program.")
#     print("1. names of student")
#     print("2. add student")
#     print("3. edit name")
#     print("4. remove student")
#     print("5. search student")
#     print("6. print all names")
#     print("7. count all number of students")
# def names_of_students():
#    print("1. Rani")
#    print("2. Budi")
#    print("3. Santi")
#    add_students(names_of_students)
# def add_students(names_of_students):
#     new_student = eval(input("add new students :"))
#     print(names_of_students)
#     print(new_student)
# def edit_name():
#     edit = eval(input(""))
print("student names program")
students = ["Rani", "Santi", "Budi"]
counter = 0
for numbers_and_names in students:
    counter = counter + 1
    print(counter,numbers_and_names)
new_students = str(input("type the name of another student :"))
students.append(new_students)
counter = 0
for names in students:
    counter = counter + 1
    print(counter,names)
choice = str(input("do you want to rename the students?(yes/no):"))
if(choice == "yes"):
    rename = str(input("whose name that you want to edit ? :"))
    rename_becomes = str(input("what names that you want to change:"))
    if(rename == "rani") or (rename == "Rani"):
        students[0] = rename_becomes
        counter = 0
        for names_change_1 in students:
            counter = counter + 1
            print(counter,names_change_1)
    elif(rename == "Santi") or (rename == "santi"):
        students[1] = rename_becomes
        counter = 0
        for names_change_2 in students:
            counter = counter + 1
            print(counter,names_change_2)
    elif(rename == "Budi") or (rename == "budi"):
        students[2] = rename_becomes
        counter = 0
        for names_change_3 in students:
            counter = counter + 1
            print(counter,names_change_3)
    elif(rename == new_students):
        students[3] = rename_becomes
        counter = 0
        for names_change_4 in students:
            counter = counter + 1
            print(names_change_4)
elif(choice == "no"):
    print("ok")
else:
    print("you must choose yes or no")
remove = str(input("do you want to remove student? (yes/no): "))
if(remove == "yes"):
    remove_names = str(input("whose names that you want to remove? :"))
    if(remove_names == "rani") or (remove_names == "Rani"):
        del students[0]
        counter = 0
        for remove_names_1 in students:
            counter = counter + 1
            print(counter,remove_names_1)
    elif(remove_names == "santi") or (remove_names == "Santi"):
        del students[1]
        counter = 0
        for remove_names_2 in students:
            counter = counter + 1
            print(counter,remove_names_2)
    elif(remove_names == "Budi") or (remove_names == "budi"):
        del students[2]
        counter = 0
        for remove_names_3 in students:
            counter = counter + 1
            print(counter,remove_names_3)
    elif(remove_names == new_students):
        del students[3]
        counter = counter + 1
        for remove_names_4 in students:
            counter = counter + 1
            print(counter,remove_names_4)
elif(remove == "no"):
    print("ok")
else:
    print("you must choose yes or no")
search = str(input("search name of students  :"))
if(search in students):
    print(search,"is in the list")
else:
    print("not found")
print("all names of students :")
counter = 0
for all_names in students:
    counter = counter + 1
    print(counter,all_names)
print("all numbers of students :", len(students))