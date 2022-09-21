#Used to determine the BMI category
def getBmiCategory(bmi):
    if bmi < 16.0:
        return 'Severe thinness'
    if bmi < 17:
        return 'Underweight (Moderate thinness)'
    if bmi < 18.5:
        return 'Underweight (Mild thinness)'
    if bmi < 25.0:
        return 'Normal range'
    if bmi < 30.0:
        return 'Overweight (Pre-obese)'
    if bmi < 35.0:
        return 'Obese (Class I)'
    if bmi < 40.0:
        return 'Obese (Class II)'
    else:
        return 'Obese (Class III)'
        
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height

#Calls the BMI category
getBmiCategory(bmi)

print('According to your BMI, you are in the', getBmiCategory(bmi), 'category and have a BMI of', round(bmi,2)) 
