#WAP to print the word present to even and odd index seperately

string = input("Enter a string : ")

# 1st way
print("even : ", string[0::2])
print("odd : ", string[1::2])

# 2nd way
even, odd = [],[]

for char_index in range(len(string)):
    if char_index%2 == 0:
        even.append(string[char_index])
    else:
        odd.append(string[char_index])

print("even : ", ''.join(even), "\nodd : ", ''.join(odd))

# Enter a string : eoeoeoeoeoeoeoeo
# even :  eeeeeeee 
# odd :  oooooooo
# prajaas@YB00617:~/Python_Patterns/patterns_practice/strings$ python3 st10.py 
# Enter a string : ashish prajapati
# even :  ahs rjpt 
# odd :  sihpaaai