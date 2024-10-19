#python counter
a=input("Enter sentence :")

print("Total no. of character: ", len(a))

#print first five character
print(a[:5])

#print last 3 character
print(a[:-3])

#check if sentence contain word "Python"
if "python" or "Python" in a:
    print("yes, Python is present.")
else:
    print("Python is absent")

