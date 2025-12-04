# Task 1: Check if a Number is Even or Odd
# This program takes an integer input and checks whether it's even or odd

def check_even_odd():
    """
    Function to check if a number is even or odd
    """
    print("Task 1: Even or Odd Number Checker")
    print("=" * 40)
    
    try:
        # Taking input from user
        number = input("Enter a number: ").strip()
        
        # Check if input is empty
        if not number:
            print("Error: No input provided. Please enter a number.")
            return
        
        # Convert to integer
        number = int(number)
        
        # Check if number is even or odd using if-else statement
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
        
        # Display the result
        print("\n" + "=" * 40)
        print(result)
        print("=" * 40)
        
    except ValueError:
        print(f"Error: '{number}' is not a valid integer. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the program
    """
    while True:
        check_even_odd()
        
        # Ask if user wants to check another number
        choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()
        
        if choice not in ['yes', 'y']:
            print("\nThank you for using the Even/Odd Checker!")
            break
        print("\n" + "-" * 40)

if __name__ == "__main__":
    main()
