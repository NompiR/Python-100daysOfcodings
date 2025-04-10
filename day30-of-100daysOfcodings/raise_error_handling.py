height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = weight / height ** 2 #or (height * height)

if height > 3:
    raise ValueError("Human's Height should not be over 3 meters.")
else:
    print(f"Your bmi is {bmi}")