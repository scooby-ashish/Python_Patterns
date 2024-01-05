num = int(input('Enter a num : '))

for i in range(num):
    for j in range(num-i):
        print(chr(64+(num-j)), end='')
    print()

