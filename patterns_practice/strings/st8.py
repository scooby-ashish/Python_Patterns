#WAP to reverse the content of string not the string

string = input("Enter a string : ")
l=[]
for i in string.split():
    l.append(i[::-1])
print(' '.join(l))

ll=[]
for j in reversed(string):
    ll.append(j)
print(' '.join(''.join(ll).split()[::-1]))

# Enter a string : ashish subbarayudu bharath muniraju prabhath raghu vijay teja
# hsihsa uduyarabbus htarahb ujarinum htahbarp uhgar yajiv ajet
# hsihsa uduyarabbus htarahb ujarinum htahbarp uhgar yajiv ajet