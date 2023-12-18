n = int(input('Enter num of rows : '))

for i in range(n):
    for j in range(n):
        print((chr(64+n-j)+' '), end=' ')
    print()