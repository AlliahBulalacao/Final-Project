
import tkinter
top = tkinter.Tk()
top.title("Dictionary")
top.mainloop()


students = {201: {"name":"Alliah Bulalacao", "year": 2003},
             202: {"name":"Eddie Santiago", "year": 2002},
         203: {"name": "Ruby Bautista", "year": 1999},
         204: {"name": "Lee Soo", "year": 1999},
         205: {"name": "Park Emma", "year": 1999},
         206: {"name": "Yoon Jenna", "year": 1999},
         207: {"name": "Kwon Linda", "year": 1999},
         208: {"name": "Momo Fidel", "year": 1999},
         209: {"name": "Hong Yujin", "year": 1999},
         210: {"name": "Moon Jun", "year": 1999},
         211: {"name": "Kim Min", "year": 1999},
         212: {"name": "Boo Kwan", "year": 1999},
         213: {"name": "Lim Resa","year": 1999},
         214: {"name": "Jeon Won", "year": 1999},
         215: {"name": "Hao Yen", "year": 1999}}

print("\t\t\t======Student Files=====\n\n")


print("Option:\n"
      "a. Clear Student File\n"
      "b. Get Student File\n"
      "c. List of Student Numbers\n"
      "d. Delete a Student File\n"
      "e. Add a Student File\n"
      "f. Display Only Student Names\n")
ask = input("What do you want to do with the student files? ")

def menu():
    if ask == "a":
        students.clear()
        print(students)

    elif ask == "b":
        file = int(input("What student file you want to get? (Please enter student number, Ex: 214): "))
        print(students.get(file))

    elif ask == "c":
        print(students.keys())

    elif ask == "d":
        file = int(input("What student file you want to delete? (Please enter student number, Ex: 214): "))
        students.pop(file)
        print(students)

    elif ask == "e":
        stud_num = input("What do you want to add? (Please enter student number, Ex: 214): ")
        name = input("What is the name of the student you want to add? ")
        students.update({stud_num: name})
        print(students)

    elif ask == "f":
        print("List of the name of students in the school files: ")
        for i in students:
            print(students[i])

    elif ask == "g":
        letter = input("Enter the letter to display the words starting with it: ")
        stud_num = int(input())
        for i in students:
            if i.startswith(letter):
                print(i)


    else:
        print("Invalid code. Please try again.")

menu()
