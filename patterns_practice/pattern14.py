n = int(input('Enter num of rows : '))

for i in range(n):
    print((chr(65+i)+' ')*(i+1))
print()

for i in range(n):
    for j in range(i+1):
        print((chr(65+i)), end=' ')
    print()
print()