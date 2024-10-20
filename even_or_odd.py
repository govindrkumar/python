#WAP to check if a number entered by the person is odd or even
#Govind Kumar Singh

x=int(input("Enter number: "))
y=x%2

if (x%2==0):
    num="even"
else:
    num="odd"

print("Number is -> ",num)
