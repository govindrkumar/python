#WAP to check if a list contains a palindrome of element. (hint: use copy() method)
movie_list=[]
movie_list.append(input("Enter no. : "))
movie_list.append(input("Enter next: "))
movie_list.append(input("Enter next: "))
movie_list.append(input("Enter next: "))
movie_list.append(input("Enter next: "))
cop1=movie_list.copy()

if (cop1==movie_list):
    print("yes, it's palindrome")
else:
    print("na, bhai")



