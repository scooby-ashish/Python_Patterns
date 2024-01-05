#WAP to convert first and last alphabet of string as upper case and remaining all should be lower case

string = input("Enter a string : ")

#print(string[0].upper()+string[1:len(string)-1].lower()+string[len(string)-1].upper())
print(string[0].upper()+string[1:-1].lower()+string[-1].upper())
