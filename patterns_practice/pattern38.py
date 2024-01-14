#inverted pyramid

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, end='')
    for j in range(num-i):
        print(chr(65+j)+' ', end='')
    print()

# Enter a num : 5
# A B C D E 
#  A B C D 
#   A B C 
#    A B 
#     A 
