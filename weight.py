print("Welcome to Weight Converter!")  
kg = float(input("Enter weight: "))
lb = round(kg * 2.2, 2)
oz = round(kg * 35.273962, 2)
print(f"In Pound: {lb:.2f} lb")  # Correct usage of f-string
print(f"In Ounce: {oz:.2f} oz")  # Correct usage of f-string

