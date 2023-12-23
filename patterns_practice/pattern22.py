num = int(input("Enter num : "))

# for i in range(num):
#     print(str(num-i)*(num-i))

for i in range(num):
    for j in range(num-i):
        print(num-i, end='')
    print()