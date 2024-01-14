#inverted pyramid with alphabets

num = int(input("Enter a num : "))

for i in range(num):
    print(' '*i, (chr(65+i)+' ')*(num-i))

# Enter a num : 5
#  A A A A A 
#   B B B B 
#    C C C 
#     D D 
#      E 