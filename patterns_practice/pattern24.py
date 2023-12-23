num = int(input("Enter num : "))

for i in range(num):
    for j in range(num-i):
        print(j+1, end='')
    print()