    # grade calculator 
a = input("enter a student name :")
x = float(input(" no.of marks in sub 1 : "))
y = float (input("no. of marks sub 2 :"))
z= float (input(" no. of marks in sub 3 :"))


total = x+y+z 
precentage = total /3 
print ("precentage ",precentage)

if precentage >= 90:
    grade = "A"
elif precentage >=80 :
    grade = "B"
elif precentage >=70 :
    grade = "c"
elif precentage >= 30:
    grade = "D"
else :
    grade = "fail"


print ("grade ", grade )


if precentage >= 40 :
    print( " result : pass ")
else :
    print( " result : fail ")

