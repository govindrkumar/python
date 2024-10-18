#Basic calculator
#Govind Kumar Singh
#19-10-2024

print("Welcome to the Basic Calculator")
x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))

#now ALU
oper=input("Enter an operator (+, -, *, /): ")

#perform calculations
if oper=='+':
    result=x+y
elif oper=='-':
    result=x-y
elif oper=='*':
    result=x*y
elif oper=='/':
    result=x/y

#Now result time Baby!!!
print("The result of ",x,oper,y,"is",result)
print("Program Ends.......")

