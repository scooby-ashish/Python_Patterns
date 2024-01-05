num = int(input('Enter a num : '))

for i in range(num):
    print(' '*(num-(i+1)), end='')
    for j in range(i+1):
        print(chr(64+num-j), end=' ')
    print()

#     E 
#    E D 
#   E D C 
#  E D C B 
# E D C B A 