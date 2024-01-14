lists = list(map(int, input('Enter a list : ').split()))
remove_ele = int(input('Enter a element to remove : '))

# for i in range(len(lists)):
#     if remove_ele in lists:
#         lists.remove(remove_ele)
   
def recursive_remove(lists, remove_ele):
    if remove_ele not in lists:
        return
    lists.remove(remove_ele)
    return recursive_remove(lists, remove_ele)

recursive_remove(lists, remove_ele)
print(lists)