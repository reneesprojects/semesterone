

#Question 1
def main():
#An empty list to store all the patient names entered
    patientnames = []

#The menu in which the hospital admin can choose which action they want
    while True:
        print()
        print("1. Add a patient's name.")
        print("2. Remove a patient's name, given its position.")
        print("3. Remove a patient's name, given its value.")
        print("4. Display all patients.")
        print("5. Search for a patient's position.")
        print("6. Display all patients in ascending order.")
        print("7. Display the number of patients.")
        print("8. Display average number of names, longest name and shortest name.")
        print("9. Quit the program.")
        print()

        choice = input("Enter your choice (1-9): ")
#The user can enter the action they want to do with the program

        if choice == '1':
            repeat = 'yes'
            while repeat.lower() == 'yes':
#allow the user to enter names
                ques1 = input("Add a patient's name: ")
#to add every name in 'ques1' to list 'patientnames'
                patientnames.append(ques1)
                print("Here is the list of patients:", patientnames)
#another choice to confirm if they want to add another names
                repeat = input("Do you want to add another name? (Yes/No): ").lower()

        elif choice == '2':
#'int' to make sure they only enter a whole number because decimals do not exist in positions
            position = int(input("Choose the position you want to remove: "))
#checks whether the provided position is valid, meaning it is a non-negative integer
            if 1 <= position < len(patientnames):
#if position is valid, this line deletes the patient name at the specified position
              del patientnames[position - 1]
              print("Here's the updated list:", patientnames)
            else:
#this outcome will be printed if position is invalid
              print("Invalid position. Patient not found in the list.")

        elif choice == '3':
#The user can choose which name to remove
            removed = input("Choose the name you want to remove: ")
#this condition will match to see if the name is inside the list and remove it
            if removed in patientnames:
              patientnames.remove(removed)
              print("Here's the updated list:", patientnames)
#If the name is not there then this message will be printed
            else:
              print("Patient not found in the list.")

        elif choice == '4':
#If the length of the name is more than 0, it will print out the names
            if len(patientnames) > 0:
              print("All Patients:", patientnames)
            else:
              print("There are no patients to be found.")

        elif choice == '5':
#The user can choose which name to find
            find = input("Which name do you want to search for?: ").lower()
            if find in patientnames:
              print("The patient has been found in position:", patientnames.index(find)+1)
            else:
              print("Patient has not been found.")

        elif choice == '6':
#This will sort the patient names into ascending order
            sortedpatients = sorted(patientnames)
            print("The ascending order is:", sortedpatients)

        elif choice == '7':
#This will print the length of the patient names
            length = len(patientnames)
            print("The number of patients is:", length)

        elif choice == '8':
#This command checks if there are any patient names in the patientnames list
            if len(patientnames) > 0:
#This creates a list called lengths containing the lengths of each patient name in the patientnames list
              lengths = [len(name) for name in patientnames]
# This calculates the average length of patient names by summing up the lengths and dividing by the total number of names
              average = sum(lengths) / len(patientnames)
#This finds the length of the longest patient name in the list
              longest = max(lengths)
#This finds the length of the shortest patient name in the list
              shortest = min(lengths)
#This creates a list of patient names that have the length equal to the longest length
              longestnames = [name for name in patientnames if len(name) == longest]
#This creates a list of patient names that have the length equal to the shortest length
              shortestnames = [name for name in patientnames if len(name) == shortest]
              print("The average number of characters in names:", average)
              print("The longest name(s) is/are:", longestnames)
              print("The shortest name(s) is/are:", shortestnames)
            else:
#If there are no names in the list, this will be printed
              print("There are no names in this list.")

#The loop will break and terminate the program if the user chooses this
        elif choice == '9':
            print("Thank you for using the program!")
            break

        else:
          print("Invalid choice. Please enter a valid option.")

main()