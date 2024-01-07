#WAP to reverse a string using slice operator and without slicing ?

string = input("Enter a string : ")

print(string[::-1])

for i in range(len(string)-1, -1, -1):
    print(string[i], end='')
print()

reversed_object = reversed(string)
print(''.join(reversed_object))

i = 0
output = ''
len_str = len(string)-1
while len_str >= i:
    output += string[len_str]
    len_str -= 1

print(output)