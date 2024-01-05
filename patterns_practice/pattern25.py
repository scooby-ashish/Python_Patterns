num = int(input("Enter a num : "))

for i in range(num):
    for j in range(num-i):
        print(num-j, end='')
    print()

