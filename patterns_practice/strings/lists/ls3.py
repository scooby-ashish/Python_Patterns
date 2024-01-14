#pop with index

lists =  [int(x) for x in input('Enter a list : ').split()]
pop_index = int(input("index : "))

while True:
    if pop_index <= len(lists)-1:
        print(lists.pop(pop_index))
    else:
        break

print(lists)

