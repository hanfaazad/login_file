# login system with multiple users

users = {
    "admin": "12345",
    "hani": "mypassword",
    "guest": "guest123"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Access granted")
else:
    print("Access denied")