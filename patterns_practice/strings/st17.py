#WAP to remove the duplicates from the string

string = input("Enter a string : ")

def remove_string_duplicate(string):
    l = ''
    if len(string) == 1:
        return string
    for ch in string:
        if ch not in l:
            l += ch
    return l

output = remove_string_duplicate(string)
print(output)