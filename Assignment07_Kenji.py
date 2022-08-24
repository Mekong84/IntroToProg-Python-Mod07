# ------------------------------------------------- #
# Title: Assignment 7
# # Description: Pickling and Structured Error Handling (Try-Except)
# # ChangeLog: (Who, When, What)
# # Kenji Petrucci, 8/22/22,Created Script
# # ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.txt'
rows = {}    # A row of data separated into elements of a dictionary
table = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb") #the b is for byte ops!
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)  # load() only loads one row of data.
    objFile.close()
    print(objFileData)

# Presentation ------------------------------------ #
while (True):
    print("""
    Please Select From the Following Menu Options:
    1) Show Current Saved Data 
    2) Add New Data
    3) Save Data to File
    4) Exit Program
    """)
    sel = input("Enter Selection [1 to 4]: ")
    print()  # adding a new line for looks
    try:
        # Show current saved data
        if (sel.strip() == '1'):
            read_data_from_file(strFileName)
            continue
        # Add a new item to the list/Table
        elif (sel.strip() == '2'):
            ID = int(input("Please enter ID number: "))
            name = input("Please enter name: ")
            if name.isnumeric():
                raise Exception("ERROR: Names must not contain numbers")
            else:
                rows = {"ID": ID, "Name": name}  # add values (user input) to defined keys
                table.append(rows)
            continue
        # Save tasks to the ToDoList.txt file
        elif (sel.strip() == '3'):
            save_data_to_file(strFileName, table)
            print('Data Saved!')
            continue
        # Exit program
        elif (sel.strip() == '4'):
            break  # and Exit the program
    except FileNotFoundError as e:
        print("ERROR: File does not exist")
    except ValueError as e:
        print("ERROR: ID must be whole integer value")
    except Exception as e:
        print(e, type(e))
