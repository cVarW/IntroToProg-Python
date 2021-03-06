# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Chloe Wei,05.13.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
strData = open(objFile, "r")
for row in strData:
    t, v = row.split(",")
    dicRow = {"Task": t, "Priority": v.strip()}
    lstTable.append(dicRow)
strData.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for row in lstTable:
            print("\t", row["Task"], ", ", row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        # 2020.05.15: Added loop for multiple additions to RAM
        strCont = "y"
        while True:
            if strCont.lower() == "y":
                strT = str(input("Enter your new task: "))
                strP = input("It's priority [1 to 5]: ")
                lstTable.append({"Task": strT, "Priority": strP})
                strCont = input("\tYou have added '"
                                + strT + "' to your 'To Do' list. \n\tDo you wish to add more? (y/n): ")
            else:
                strCont = "n"
                break
        print("\tYour new 'To Do' list is: ")
        for row in lstTable:
            print("\t\t", row["Task"], ", ", row["Priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        # 2020.05.15: Added feedback
        #   decided against looping, may consider 'undo' down the road
        strI = str(input("What task do you want to remove: "))
        for row in lstTable:
            if row["Task"].lower() == strI.lower():
                lstTable.remove(row)
                print("Task '" + strI + "' was removed from your list.")
        if row["Task"].lower() != strI.lower():
                print("\tTask is not in 'To Do' list.")
        else:
            continue
        # for row in lstTable:
        #        print("\t\t", row["Task"], ", ", row["Priority"])
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        strData = open(objFile, "w")
        for row in lstTable:
            strData.write(str(row["Task"]) +
                          "," + str(row["Priority"] + "\n"))
        strData.close()
        print("All tasks saved to ToDoList.txt!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        input("Press enter key to exit.")
        break  # and Exit the program
