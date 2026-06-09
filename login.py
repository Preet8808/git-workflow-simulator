def login(user, password):
    if user == "admin" and password == "1234":
        return "Login Successful"
    return "Login Failed"

if __name__ == "__main__":
    print(login("admin", "1234"))
