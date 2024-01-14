#inverted pyramid 

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, end='')
    for j in range(num-i):
        print(f'{j+1} ', end='')
    print()

# Enter a num : 5
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 