#inverted pyramid

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, end='')
    for j in range(num, i, -1):
        print(chr(64+j)+' ', end='')
    print()

# Enter a num : 5
# E D C B A 
#  E D C B 
#   E D C 
#    E D 
#     E 