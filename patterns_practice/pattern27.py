num = int(input('Enter a num : '))

# for i in range(num):
#     for j in range(num-(i+1)):
#         print(' ', end='')
#     for k in range(i+1):
#         print('* ', end='')
#     print()

for i in range(num):
    print((num-(i+1))*' '+'* '*(i+1))

