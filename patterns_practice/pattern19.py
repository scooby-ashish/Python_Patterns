num = int(input('Enter the num : '))

# for i in range(num):
#     print('*'*(num-i))

for i in range(num):
    for j in range(num-i):
        print('*', end='')
    print()