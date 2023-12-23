num = int(input("Enter num : "))

for i in range(num):
    print(chr(64+(num-i))*(num-i))

for i in range(num):
    for j in range(num-i):
        print(chr(64+(num-i)), end='')
    print()