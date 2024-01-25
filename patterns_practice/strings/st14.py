#WAP which returns multiple of strings in a sorted way
# x3a2g1s2 -->> aagssxxx

string = input("Enter a string : ")

def sorted_string_repetition(string):
    full_sorted_string = ''; temp=''
    if len(string) == 1:
        return string
    for i in range(len(string)):
        if string[i].isalpha():
            temp += string[i]
        else:
            full_sorted_string += (temp*int(string[i]))
            temp = ''
    if len(temp) != 0:
        full_sorted_string += temp
    return ''.join(sorted(full_sorted_string))

output = sorted_string_repetition(string)
print(output)

