# Define a function to calculate BMI
def calculate_bmi(weight, height):
    #return weight / (height ** 2)
    height_meters = height / 100
    return weight / (height_meters ** 2)

# Define a function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Define the main function
def main():
    # Prompt user for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height_cm)

    # Classify BMI
    bmi_category = classify_bmi(bmi)

    # Display BMI result and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {bmi_category}")

# Check if this file is being run directly
if __name__ == "__main__":
    main()  # Call the main function if the file is run directly
