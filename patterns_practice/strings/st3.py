# take username and password and compare username can be case-insensitive but password cannot be case-sensitive

username = input("Username : ").lower()
password = input("Password : ")

if username == 'durga' and password == 'anushka':
    print("valid user")
else:
    print("invalid user")