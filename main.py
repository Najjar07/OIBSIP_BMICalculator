# BMI Calculator

print("=== BMI Calculator ===")

# Get user weight
weight = float(input("Enter your weight in kg: "))

# Get user height
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI
print("Your BMI is:", round(bmi, 2))

# BMI Categories
if bmi < 18.5:

    print("Category: Underweight")

elif bmi < 25:

    print("Category: Normal weight")

elif bmi < 30:

    print("Category: Overweight")

else:

    print("Category: Obese")