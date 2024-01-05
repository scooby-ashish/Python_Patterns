#WAP to check the type of character entered from the keyboard

string = input('Enter a character : ').strip()

if string == '':
    print("It is a empty string")
elif string.isalpha():
    if string.isupper():
        print(f"{string} is upper and a alpha")
    elif string.islower():
        print(f"{string} is lower and a alpha")
    elif string.istitle():
        print(f"{string} is in title case and a alpha")
    elif string.lower():
        print(f"{string} in between some other case converted into lower case and verified.")
elif string.isdigit():
    print(f"{string} is a digit")
elif string.isalnum():
    if string.isupper():
        print(f"{string} is upper and a alnum")
    elif string.islower():
        print(f"{string} is lower and a alnum")
    elif string.istitle():
        print(f"{string} is in title case and a alnum")
    elif string.lower():
        print(f"{string} in between some other case converted into lower alnum case and verified.")
elif string.isspace():
    print("it is just space.")
else:
    print(f"{string} may contain special characters.")