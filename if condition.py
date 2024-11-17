Height = float(input("Enter height in meters:"))
print()

Weight = float(input("Enter the weight in kilograms:"))
print()

BMI = float(Weight / Height**2)
print(BMI)
print()

if BMI >=30:
    print("Obesity")
elif 25 <= BMI <=29:
    print("Overweight")
elif 18.5 <= BMI <= 25:
    print("Normal")
else:
    print("Underweight")    
print()

