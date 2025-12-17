#This is the first version
students = []
marks_math = []
marks_computer_science = []
marks_physics = []
marks_chemistry = []
marks_biology = []

answer = input('''Welcome to student performance manager. Please select between the numbers to let us know what you want to do:
1-Continue to the menu
2-Exit
Enter: ''')
while  answer.lower() != "exit":
 answer = input(''' Please select between the numbers to let us know what you want to do:
1- Add student and their marks
2-View student
3-Get average
4-View student marks
5-Exit
Enter: ''')
 if answer == "1" or answer.lower()== "add student and their marks":
     student_name = input("Enter  name: ")
     print("Ok student name added. ")
     math_mark = int(input("Enter their math mark: "))
     print("Ok, math mark added")
     computer_science_mark= int(input("Enter computer science mark: "))
     print("Ok, computer science mark added")
     physics_mark = int(input("Enter their physics mark: "))
     print("Ok, physics mark added")
     chemistry_mark = int(input("Enter chemistry mark: "))
     print("Ok, enter chemistry mark added")
     biology_mark =int(input("Enter biology mark"))
     print("Ok, biology mark has been added")
     students.append(student_name)
     marks_math.append(math_mark)
     marks_computer_science.append(computer_science_mark)
     marks_physics.append(physics_mark)
     marks_chemistry.append(chemistry_mark)
     marks_biology.append(biology_mark)
 elif answer  == "2" or answer .lower() == "view student":
     a = input("Do you want all student name  or specific student marks")
     if a.lower() == "all student name":
       print("Wait for a minute, we are preparing the resources ")
       print("Your students are: ",students)
     elif a.lower() == "specific student grades":
        student_number = int(input("Enter the number of the student"))
        b = student_number-1
        average_1= (marks_math[b]+marks_computer_science[b]+marks_physics[b]+marks_chemistry[b]+marks_biology[b])/5
        if average_1 >= 90:
             print("This student, has achieved excellent grades in his subjects")
             print("His marks are: ",marks_math[b],marks_computer_science[b],marks_physics[b],marks_chemistry[b],marks_biology[b])
        elif average_1 >= 80 and average_1 < 90:
             print("This is a good achievement from this student, he got ", average_1,"as his average")
             print("His marks are: ",marks_math[b],marks_computer_science[b],marks_physics[b],marks_chemistry[b],marks_biology[b] )
        pass
 elif answer =="4" or answer.lower() =="view student marks":
    print("The math marks are: ",marks_math)
    print("The computer science marks: ",marks_computer_science)
    print("The physics marks are: ",marks_physics)
    print("The chemistry marks are: ",marks_chemistry)
    print("Yhe biology marks are: ",marks_biology)
 elif answer =="3" or answer.lower() == "get average":
   print(students)
   human_number = int(input("Please enter the number of the student: "))
   computer_number = human_number - 1
   average = (marks_math[computer_number]+marks_computer_science[computer_number]+marks_physics[computer_number]+marks_chemistry[computer_number]+marks_biology[computer_number])/5
   print(average)
 elif answer == "5" or answer.lower() == "exit":
       exit()
 else:
    print("Invalid entry")





