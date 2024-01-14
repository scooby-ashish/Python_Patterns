#inverted pyramid

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, end='')
    for j in range(num, i+0, -1):
        print(f'{j} ', end='')
    print()

# Enter a num : 5
# 5 4 3 2 1 
#  5 4 3 2 
#   5 4 3 
#    5 4 
#     5 