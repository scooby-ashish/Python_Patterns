num = int(input('Enter a num : '))

for i in range(num):
    print(' '*(num-(i+1)), end='')
    for j in range(i+1):
        print(chr(64+(j+1)), end=' ')
    print()

#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 