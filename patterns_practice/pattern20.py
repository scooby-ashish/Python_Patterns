num = int(input("Enter the num : "))

# for i in range(num):
#     print(f'{i+1}'*(num-i))

for i in range(num):
    for j in range(num-i):
        print(i+1, end=' ')
    print()