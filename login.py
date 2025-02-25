# #Task:  User Sign-up/login info
# 1.create empty array
# 2.create dictionary for each user containing name,email Id,password.
# 3.user will put data during Sign-up 
# 4.then he will login ....if matches with previous data ...pass...or fail
# 5.data for user1,user2,user3....user n...will be saved
# 6.it will come in tabular form
# 7.I can delete any user data too



from prettytable import PrettyTable 
users = []
def sign_up():
    user = {}  
    user["name"] = input("Enter Name: ")
    user["email"] = input("Enter Email: ")
    user["password"] = input("Enter Password: ")
    users.append(user)  
    print("Sign-up successful!\n")

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    for user in users:  
        if user["email"] == email and user["password"] == password:
            print("Login successful!\n")
            return
    print("Login failed! Incorrect email or password.\n")

def show_users():
    if not users:
        print("No users available.\n")
        return

    table = PrettyTable(["Name", "Email"])  
    for user in users:
        table.add_row([user["name"], user["email"]])
    
    print("\nRegistered Users:")
    print(table)

def delete_user():
    email = input("Enter Email to delete: ")
    
    for user in users:  
        if user["email"] == email:
            users.remove(user)
            print("User deleted.\n")
            return
    print("User not found.\n")

while True:
    print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        show_users()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
