#WAP to count a alphabet in a string and return with its count
#input = aaaabbbccz output=a4b3c2z

string = input("Enter a string : ")

def string_concatenate_number(string):
    output = ''; lists = []
    if len(string) == 1:
        return string
    for i in range(len(string)):
        if string[i] not in lists:
            lists.append(string[i])
            output += (string[i]+str(string.count(string[i])))
        else:
            pass
    return output

answer = string_concatenate_number(string)
print(answer)
    