num = int(input('Enter a num : '))

for i in range(num):
    print(' '*(num-(i+1)), end='')
    for j in range(i+1):
        print(f'{num-j}', end=' ')
    print()

#     5 
#    5 4 
#   5 4 3 
#  5 4 3 2 
# 5 4 3 2 1 