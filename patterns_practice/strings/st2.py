#found the substring along with its indexes

string = input("Enter a string : ")
substring = input("Enter a substring : ")

string_length = len(string)
i = 0
substring_count = 0

# while i < string_length:
#     found = string.find(substring, i, string_length)
#     if found == -1:
#         break
#     substring_count += 1
#     print(f"{substring} found at index {found}")
#     i = found + 1

# while i < string_length:
#     try:
#         found = string.index(substring, i, string_length)
#     except ValueError:
#         break
#     substring_count += 1
#     print(f"{substring} found at index {found}")
#     i = found + 1

i = string.find(substring) #ababaa   ab
if i == -1:
    print("Substring not found")
while i != -1:
    found = string.find(substring, i, string_length)
    if found == -1:
        break
    substring_count += 1
    print(f"{substring} found at index {found}")
    i = found+1

print(f"Substring count is : {substring_count}")

