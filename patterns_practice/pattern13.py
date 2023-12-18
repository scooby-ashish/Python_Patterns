n = int(input('Enter num of rows : '))

for i in range(n):
    print(f'{i+1} '*(i+1))
print()

for i in range(n):
    for j in range(i+1):
        print(f'{i+1} ', end='')
    print()