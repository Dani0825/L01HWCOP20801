##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {}
 

  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
while True :
    user_choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()
 

   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
    if user_choice == "A":
        name = input("Enter the name of the student: ")

        if name in grades:
            print("Sorry, that student is already present.")
        else:
            grade_input = input("Enter the student's grade: ")

            if not grade_input.isdigit():
                print("Please enter grade as number 0-100")
            else:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("Please enter grade as number 0-100")
                else:
                    grades[name] = grade

 

   # Handle removing a student if user inputs 'R'
   # Check input for "What student do you want to remove? "
   # use pop to remove key/value form grades
   # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
   # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
    elif user_choice == "R":
        name_remove = input("What student do you want to remove? ")

        if name_remove in grades:
            grades.pop(name_remove)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")


   # Handle modifying a student grade if user inputs 'M'
   # "Enter the name of the student to modify: "
   # Convert grade into integer
   # If student is in grades dictionary, show existing grade "The old grade is"
   # Gather input for new grade "Enter the new grade: "
   # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
    elif user_choice == "M":
        name_modify = input("Enter the name of the student to modify: ")

        if name_modify in grades:
            print(f"The old grade is {grades[name_modify]}")
            grade_input = input("Enter the new grade: ")

            if not grade_input.isdigit():
                print("Please enter grade as number 0-100")
            else:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("Please enter grade as number 0-100")
                else:
                    grades[name_modify] = grade

        else:
            print("Sorry, that student doesn't exist and couldn't be modified.")


 
   # Handle printing grade average as a string if user input is 'P'
   # Use "The average grade is "
   # Handle printing all of the student names with associated grade
   # Display explictly as strings
    elif user_choice == "P":
        if len(grades) == 0:
            print("No students to display.")
        else:
            total = 0
            for grade in grades.values():
                total += grade

            average = total / len(grades)
            print(f"The average grade is {average}.")

            for name, grade in grades.items():
                print(f" {name} has a grade of {grade}")
 
      

   # Handle the case for quiting if user inputs 'Q' "Goodbye!"
    elif user_choice == "Q" :
        print("Goodbye!")
        break

    
    # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    else:
        print("Sorry, that wasn't a valid choice.")