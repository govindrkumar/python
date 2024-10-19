"""
create a python program that asks user for a sentence, then performs the slicing and indexing
"""
print("Welcome to Our Sentence Glider!")
a=str(input("Enter your Sentence : ")
        )

#now slicing starts
print(a[:5])

print(a[-3:]) #print last three character
print(a[2:8]) #print the char from index 2 to index 8

#reverse sentence
def reverse_sentence(sentence): #declare a variable sentence
    return " ".join(sentence.split(" ")[::-1]) #using return function to remove extra space and print from slicing -1 char one by one
print(reverse_sentence(a))

#print every second character
print(a[::2])
