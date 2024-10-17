# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # Formula for BMI
    return bmi
# Function to determine BMI category based on the value
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
# Main program
def main():
    print("Welcome to the BMI Calculator!")
    # Input weight and height from the user
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        # Determine the BMI category
        category = bmi_category(bmi)
        # Output the results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
# Run the main program
if __name__ == "__main__":
    main()
