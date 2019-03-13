# Title: Assignment05
# Dev: Matt Salgado
# Create Date: Mar 12, 2019
# Change Log: File Creation

"""
Script Requirements:
1. Create the text file
2. Load data from text file into a list
3. Loop the user thru the 6 menu options and complete the action based on the user input
"""

# Step 1: Create the text file
dict1 = {"CleanHouse": "Low", "PayBills": "High"}
myToDoFile = open("/Users/matt/Desktop/ToDo.txt", "a")
myToDoFile.write(str(dict1))
myToDoFile.close()

# Step 2: Load data from text file into a list
fileOne = open("/Users/matt/Desktop/ToDo.txt", "r")
myTable = []
for line in fileOne.readlines():
    key = line.split(",")[0]
    value = line.strip().split(",")[1]
    dictRow = {key: value}
    myTable.append(dictRow)

# Step 3: Loop the user thru the menu options
while True:
    print('''
        Enter a number for your menu option:
        1) Show current data in File
        2) Show current data in List Table
        3) Add an item to the List Table
        4) Remove an existing item from the List Table
        5) Save List Table to File
        6) Exit Program
        ''')
    userInput = (input("Enter the number for the next menu option you wish to proceed with: "))

    # Step 4: For option 1, display contents of text file
    if userInput == "1":
        fileOne = open("/Users/matt/Desktop/ToDo.txt", "a")
        print(fileOne.read())
        continue

    # Step 5: For option 2, display list
    elif userInput == "2":
        print(myTable)
        continue

    # Step 6: For option 3, add item to list
    elif userInput == "3":
        taskName = (input("Enter the task name you wish to add: ").strip())
        taskPriority = (input("Enter the task priority: ").strip())
        addRow = dict({taskName: taskPriority})
        myTable.append(addRow)
        continue

    # Step 7: For option 4, remove item from list
    elif userInput == "4":
        intRemove = int(input("Which menu number do you wish to remove? "))
        myTable.pop(intRemove - 1)
        continue

    # Step 8: For option 5, save data to text file
    elif userInput == "5":
        fileOne = open("/Users/matt/Desktop/ToDo.txt", "a")
        myTable = (str(myTable)).replace(",", "\n").replace(":", ",")
        chars = "{}[]'"

        for c in chars:
            myTable = myTable.replace(c, "")
        myToDoFile.write("\n" + myTable + "\n")
        fileOne.close()
        continue
    # Step 9: For option 6, exit the program
    elif userInput == "6":
        break



