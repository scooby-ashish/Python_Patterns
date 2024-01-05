num = int(input('Enter a num : '))

# for i in range(num):
#     for j in range(num-(i+1)):
#         print(' ', end='')
#     for k in range(i+1):
#         print(f'{k+1} ', end='')
#     print()

for i in range(num):
    print(' '*(num-(i+1)), end='')
    for j in range(i+1):
        print(j+1, end=' ')
    print()
