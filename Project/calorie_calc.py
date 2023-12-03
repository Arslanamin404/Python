def calculate_calories(gender, weight, height, age):
    if gender == 'm':
        BMR = 66.5+(13.75*weight)+(5.003*height)-(6.755*age)
    else:
        BMR = 655+(9.6*weight)+(1.8*height)-(4.7*age)
    
    print("\n#############################################################################################################\n")    
    print(f"\tThe estimated Base Metabolic Rate for you is approximately {round(BMR,2)} calories per day.")
    print("\n#############################################################################################################\n")    
    

def main_func():
    print("Welcome to the Calorie Calculator\n")
    while True:
        try:
            gender = input("Enter Your Gender [M] Male or [F] Female [M/F]: ").lower()
            
            if gender not in ['m', 'f']:
                raise ValueError("Invalid input for gender. Please enter 'M' or 'F'.")
            
            weight = float(input("\nEnter your Weight (kg): "))
            height = float(input("\nEnter your Height (cm): "))
            age = int(input("\nEnter your age: "))
            
            if weight <=0 or height<=0 or age <=0:
                raise ValueError("Weight, Height, and Age must be positive values.")
            
            calculate_calories(gender, weight, height, age)
            while True:
                exit_choice = input("Do you want to calculate again? [yes/no]: ").lower()
                if exit_choice in ['yes', 'no']:
                    print("\nExiting. . . \n\n")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if exit_choice == 'no':
                break
            
        except ValueError as valErr:
            print(f"\nERROR: {valErr}\n")
        except Exception as err:
            print(f"Something unexpected has occurred: {err}\n")

if __name__ == "__main__":
    main_func()
