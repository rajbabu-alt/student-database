class Student:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def display_info(self):
        print(f"name is {self.name},age is {self.age}, roll_no is {self.rollno}")
students = []

while True:
    print("\n welcome to student database ")
    print("1.Add a student ")
    print("2.View the entire database ")
    print("3.Search a student ")
    print("4.Exit the database ")

    choice = int(input("enter your choice according to the requirement from 1 to 4 : "))
    if choice == 1:
        name = input("enter your name : ")
        age = int(input("enter your age : "))
        rollno = int(input("enter your roll_no :"))
        student = Student(name,age,rollno)
        students.append(student)
        print("student successfully added to the database")
    elif choice == 2:
        print("\n welcome to student database ")
        for s in students:
         s.display_info()


    elif choice == 3 :
        search_student = input("enter the student name you want to search : ")
        found = False

        for s in students:
          if s.name.lower() == search_student.lower():
            s.display_info()
            found = True
            break
        if not found:
           print("unable to find the student ")

    elif choice == 4:
         print("bye have a nice day")
         break

    else:
      print("invalid choice.")























