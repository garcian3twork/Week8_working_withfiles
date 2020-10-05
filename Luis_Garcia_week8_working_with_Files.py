#Author Luis Garcia
#version 1.0 as I will be using this for other projects


import os



#gather and show information that will assist the user in chosing directories and files
current_directory = os.getcwd()
print(f"\nYour current directory is {current_directory}")
print("\nWith this application you will create a directory and a file, if you do not specify a direct path")
print(f"for your directory, your directory will be saved under {current_directory}.")
user_directory = input("What directory would you like to save you file in?: ")
user_file = input("What is your file name?: ")
user_file = user_file + ".txt"
full_path = (f'{user_directory}\\{user_file}')

#Gather user information
user_name = input("What is your name?: ")
user_address = input("What is your address?: ")
user_phone = input("What is your phone number?: ")
user_profile = (f'{user_name.title()} , {user_address.title()} , {user_phone}')



#This is to check if the chosen directory exists
if os.path.isdir(user_directory):
    print("Directory exists , checking file next --> moving on")#If the directory exists we will move on to check the file
else:
    os.makedirs(user_directory)#Creates directory if non existent
    print(f"Directory {user_directory} created.")#lets the user know the directory path and that it was created

if os.path.isfile(full_path):#This checks if the user file exists
    print("File already exists")
else:
    try:
        if not os.path.exists(full_path):
            with open(os.path.join(user_directory, user_file), 'w+') as file_1:#creates the file under the user specified directory
                file_1.write(user_profile)#writes the information gathered from the user under the user_profile variable
                file_1.seek(0)#use the seek method to set the current position of the file to 0
                text = file_1.readlines()# this allows shows the user the file contents as program output
                print(f"\nThe following information has been saved: {text}  --- added to file ---> {full_path}")
    except FileExistsError:#in the event of any exceptions
        print("File exists")
