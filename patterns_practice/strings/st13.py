#WAP to convert string if input as a4b3c2 to aaaabbbcc

string = input('Enter a string : ')

def string_repetition(string):
    full_string, temp = '', ''
    if len(string) == 1:
        return string
    else:
        for i in range(len(string)):
            if string[i].isalpha():
                temp += string[i]
            else:
                full_string += (temp*int(string[i]))
                temp = ''
    if len(temp) != 0:
        full_string += temp
    return full_string

output = string_repetition(string)
print(output)
