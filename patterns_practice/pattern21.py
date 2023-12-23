num = int(input("Enter num : "))

# for i in range(num):
#     print(chr(64+i+1)*(num-i))

for i in range(num):
    for j in range(num-i):
        print(chr(65+i), end='')
    print()