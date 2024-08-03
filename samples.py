# we are creating a secure login system in python
# road to cybersecurity
import hashlib
import os
import csv


def hash_password(password):
    # create a new salt
    salt = os.urandom(16)  # random numbers produced by the operating system
    # salt is a random piece of data added to a password before it is hashed and stored
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    # this created the has using the salt and password
    return salt, hashed_password


def verify_password(stored_password, stored_salt, provided_password):
    # we are hashing the provided pass with the stored salt
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", provided_password.encode(), stored_salt, 100000
    )
    # this is comparing the hashed password with the stored password
    return hashed_password == stored_password


def register_user(username, password):
    salt, hashed_password = hash_password(password)
    file_exists = os.path.isfile("users.csv") #this is checking if the file named users.csv exists in the current directory 
    with open("users.csv", "a", newline="") as file: #we open the file users.csv in append mode which is the "a"
        #newline makes sure that newlines are handled 
        #file is used as an object
        writer = csv.writer(file)#writes the data to the file 
        if not file_exists:
            #making sure the file exists
            writer.writerow(
                ["Username", "Salt", "Hashed_Password"]
            )  # Write header if file doesn't exist
        writer.writerow([username, salt.hex(), hashed_password.hex()])
    print("User registered successfully!")


def login_user(username, password):
    if not os.path.isfile("users.csv"):
        print("No users are registered yet. Please register first.")
        return False
    with open("users.csv", "r") as file:
        #opening the file in read mode
        reader = csv.reader(file) #the csv.reader part is creating an object that will read from file
        next(reader)  # Skip the header
        for row in reader: #this is checking each row in the file which is now called reader
            stored_username, stored_salt, stored_password = row #it stores the values from each row into these
            if stored_username == username: #checks if the same user 
                if verify_password(
                    bytes.fromhex(stored_password), bytes.fromhex(stored_salt), password #this whole process checks if the passwords are the same
                ):
                    print("Login successful!")
                    return True
                else:
                    print("Invalid password.")
                    return False
        print("Username not found.")
        return False


def main():
    while True:
        print("\nSecure Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
