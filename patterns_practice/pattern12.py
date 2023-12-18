n = int(input('Enter num of rows : '))

for i in range(n):
    print('* '*(i+1))
print()

for i in range(n):
    for j in range(i+1):
        print('* ', end='')
    print()

