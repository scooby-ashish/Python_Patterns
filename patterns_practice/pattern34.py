#need to print the inverted pyramid

num = int(input("Enter a number : "))

for i in range(num):
    print(" "*i,"* "*(num-i))


# Enter a number : 5
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 