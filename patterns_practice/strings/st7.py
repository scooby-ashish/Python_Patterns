#WAP to reverse order of words

string = input("Enter a string : ")

l = string.split()
print(' '.join(l[::-1]))

for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')
print()

