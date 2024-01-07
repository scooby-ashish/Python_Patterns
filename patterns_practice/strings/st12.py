#WAP to seperate alphabets and digits from string and print as firstString followed by digits

string = input("Enter a string : ")

l1,l2=[],[]

for i in string:
    if i.isalpha():
        l1.append(i)
    elif i.isdigit():
        l2.append(i)

print(''.join(sorted(l1)+sorted(l2)))
l1.sort()
l2.sort()
print(''.join(l1)+''.join(l2))

# Enter a string : a1b2c3d4e5
# abcde12345