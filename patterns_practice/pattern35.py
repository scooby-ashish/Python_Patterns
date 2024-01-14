#inverted pattern with fixed numbers

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, f'{i+1} '*(num-i))


# Enter a num : 5
#  1 1 1 1 1 
#   2 2 2 2 
#    3 3 3 
#     4 4 
#      5 