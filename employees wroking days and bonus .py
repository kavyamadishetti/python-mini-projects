#  employees wroking days and bonus 
a = input (" Enter a name of the employee:")
b = int (input(" Enter a total no. of working days : " )) 
c= int(input("Enter a total no . of present days :"))


precentage = ( c/ b)*100 
print ("precentage",precentage )

if precentage >= 90 :
    print("got bonus")
else :
    print(" not approved ")