#pop elements from list

lists = list(map(int, input("Enter a list : ").split()))
print(lists)
while True:
    if len(lists) == 0:
        break
    else:
        lists.pop()
print(lists)
print(lists.pop())