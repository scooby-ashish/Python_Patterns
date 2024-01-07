#wAP to reverse every second word of a string 

string = input("Enter a string : ").split()

empty_list = []

if len(string) == 1: #if length of string is one then print as it is
    print(''.join(string))
else:
    for s_word in range(len(string)): # 0 to len(string)-1
        if s_word % 2 != 0: # 0, 1/2!=0, 2, 3/2!=0, 4, 5/2!=0, 6
            empty_list.append(string[s_word][::-1]) # appending element in reverse order
        else:
            empty_list.append(string[s_word]) # element with index 0, 2, 4, 6
    print(' '.join(empty_list)) #join list with a space

# Enter a string : one two three four five six
# one owt three ruof five xis
    
