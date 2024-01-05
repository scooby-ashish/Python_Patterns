#WAP to display characters of given string index wise.

word = input("Enter a word : ")

length = len(word)

for i in range(length):
    print(word[i],' forward index : ', i, ' backward index : ', -(length-i))

# word - durga
# length = 5 #0,1,2,3,4
# 'd' forward index : 0 backward index : -5
# 'u' forward index : 1 backward index : -4