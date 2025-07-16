username = "admin"
password = "12345"

entered_username = input("Enter your username:  ")

enter_password = input("Enter your password:  ")

if entered_username == username and enter_password == password:
    print("Login successfully!  Welcome" )

elif entered_username == username and enter_password != password:
    print("Incorrect password. Please Try again")    

elif entered_username != username and enter_password == password:
    print("Incorrect username!")

else:
    print("Incorrect information! Try again.")