n = int(input('Enter num of rows : '))

for i in range(n):
    for j in range(n):
        print(chr(65+j), end=' ')
    print()