#BMI

#input
we = float(input("Weight (kg): "))
he = float(input("Height (m): "))

#Process
bmi = we/((he)**2)

#output
if bmi < 18.5:
    print("BMI is {:.1f}".format(bmi))
    print("Underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("BMI is {:.1f}".format(bmi))
    print("Normal weight")
elif bmi >= 25 and bmi < 30 :
    print("BMI is {:.1f}".format(bmi))
    print("Overweight")
else :
    print("BMI is {:.1f}".format(bmi))
    print("Obesity")