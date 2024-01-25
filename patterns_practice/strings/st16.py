#WAP to
#input - a4k3b2
#output - aeknbd

string = input("Enter a string : ")

def string_forwd_char(string):
    fstring = ''; temp_ord = 0
    if len(string) == 1:
        return string
    for i in range(len(string)):
        if string[i].isalpha():
            temp_ord = ord(string[i])
            fstring += string[i]
        else:
            chrOf = chr(temp_ord+int(string[i]))
            fstring += chrOf
            temp_ord = 0
    return fstring

output = string_forwd_char(string)
print(output)