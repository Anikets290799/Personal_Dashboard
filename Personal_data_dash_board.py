import json
import os
database = "data.json"
data = []

def load_data():  #loades the data from Json database
    global data
    if os.path.exists(database):
        with open(database) as fs:
            data.extend(json.load(fs))

def save_file():  # saves the file in Json 
    with open(database,"w") as fs:
        json.dump(data,fs)



def add_entries():
    name = input("Tell your name: ")
    age = int(input("Tell your age: "))
    eduction = input("Tell your eduction Detail: ")
    address = input("Tell your address: ")
    city = input("Tell your city: ")
    phone_no = input("Tell your number: ")
    hobbies = input("Tell your hobbies: ").split(" ")

    entity = {
        "name": name.strip(),
        "age" : age,
        "eduction" : eduction,
        "address" : address,
        "city" : city,
        "number" : phone_no,
        "hobbies" : hobbies,
        }

    data.append(entity)
    save_file()
    print("Data added sucessfully",entity)



def view_entries():
    load_data()
    print("Showing all entries..")
    if not data:
        print("No entries found.")
        return
    for i, entity in enumerate(data, start=1):
        print(f"{i}. {entity}")
    print()

def find_entries():
    load_data()
    name = input("tell me the name: ").lower().strip()
    found = False
    for entity in data:
        if (entity["name"].strip().lower() == name.lower()):
            print("Found",entity)
            found = True
            break
    if not found:
        print("The entered name not found..!")

def del_entries():
    load_data()
    name = input("Tell me the name for which you wnt to delete the entries: ").strip()
    for i,entity in enumerate(data):
        if (entity["name"].lower() == name.lower()):
            data.pop(i)
            save_file()
            print("The entry deleted..!")
            return
    print("Name not found")

def call():
    while True:
        print("Welcome to your personal Dashboard..!")
        print("Please select any one of the action..!")
        print("1. To add entries..!")
        print("2. To view entries..!")
        print("3. To Search by Name..!")
        print("4. To Delete the entries..! ")
        print("5. Exit")

        choice = int(input("Please enter any of the choies: "))
        if (choice == 1):
            add_entries()
        elif (choice == 2):
            view_entries()
        elif(choice == 3):
            find_entries()
        elif(choice == 4):
            del_entries()
        elif(choice == 5):
            print("Thank you..!")
            break
        else:
            print("Enter the correct Number..!")

call()
