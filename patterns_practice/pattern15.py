n = int(input('Enter num of rows : '))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    print()