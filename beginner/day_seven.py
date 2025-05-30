#BMI function

def body_mass_index(weight:float, height:float):
    if weight<=0:
        print("Invalid weight, must be greater than zero.")
        return
    if height<=0:
        print("Invalid height, must be greater than zero.")
        return
    bmi = weight/(height**2)
    bmi = round(bmi, 1)
    
    if bmi < 18.5:
        return f"{bmi}, Category 'Under weight'."
    elif 18.5 <= bmi  <= 24.9:
        return f"{bmi}, Category 'Normal weight'."
    elif 25 <= bmi <= 29.9:
        return f"{bmi}, Category 'Over weight'."
    else:
        return f"{bmi}, Category 'Obese'."
def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        result = body_mass_index(weight, height)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
main()