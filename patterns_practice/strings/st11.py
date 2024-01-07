#WAP to print merge characters of two strings alternatively

string1, string2 = input("Enter two strings : ").split()

merge_string = []

i,j = 0,0

"""
if you use "or" logical operator instead of "and" in while loop then so let's say if length of 
first word = 3 
second word = 5
now i becomes 3 and j also becomes 3 
so now when you get inside the loop because False OR True is True and while appending the string1[i|3] you'll get indexerror
as the length of index is 3 but no element exists at index 3 "012" not 3
""" 
while i < len(string1) and j < len(string2): # one, two
    merge_string.append(string1[i])
    merge_string.append(string2[j])
    i += 1
    j += 1

if i < len(string1):
    merge_string.append(string1[i:])
if j < len(string2):
    merge_string.append(string2[j:])

print(''.join(merge_string))

# Enter two strings : one three
# otnheree