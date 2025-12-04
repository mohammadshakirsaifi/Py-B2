# Task 2: Sum of Integers from 1 to 50 Using a Loop
# This program calculates the sum of all integers from 1 to 50

def calculate_sum_using_for_loop():
    """
    Function to calculate sum of numbers from 1 to 50 using for loop
    """
    total = 0
    
    print("Calculating sum using for loop...")
    # Using for loop to iterate from 1 to 50 (inclusive)
    for number in range(1, 51):
        total += number
        
    return total

def calculate_sum_using_while_loop():
    """
    Function to calculate sum of numbers from 1 to 50 using while loop
    """
    total = 0
    number = 1
    
    print("Calculating sum using while loop...")
    # Using while loop to iterate from 1 to 50 (inclusive)
    while number <= 50:
        total += number
        number += 1
        
    return total

def calculate_sum_using_formula():
    """
    Function to calculate sum using mathematical formula (for verification)
    Sum of first n natural numbers = n * (n + 1) / 2
    """
    n = 50
    return n * (n + 1) // 2

def main():
    """
    Main function to run the program
    """
    print("Task 2: Sum of Integers from 1 to 50")
    print("=" * 40)
    
    try:
        # Method 1: Using for loop (as per task requirement)
        sum_for_loop = calculate_sum_using_for_loop()
        
        # Method 2: Using while loop (alternative method)
        sum_while_loop = calculate_sum_using_while_loop()
        
        # Method 3: Using formula (for verification)
        sum_formula = calculate_sum_using_formula()
        
        # Display results
        print("\n" + "=" * 40)
        print("RESULTS:")
        print("=" * 40)
        
        print(f"Sum using for loop (1 to 50): {sum_for_loop}")
        print(f"Sum using while loop (1 to 50): {sum_while_loop}")
        print(f"Sum using mathematical formula: {sum_formula}")
        
        # Verification
        if sum_for_loop == sum_while_loop == sum_formula:
            print("\n✓ All methods give the same result!")
        
        print("\n" + "=" * 40)
        print("Summary:")
        print("=" * 40)
        print(f"The sum of numbers from 1 to 50 is: {sum_for_loop}")
        
        # Additional information
        print("\nFormula used for verification:")
        print("Sum of first n natural numbers = n * (n + 1) / 2")
        print("For n = 50: 50 * 51 / 2 = 1275")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def advanced_version():
    """
    Advanced version that allows user to specify range
    """
    print("\n" + "=" * 40)
    print("ADVANCED VERSION: Custom Range")
    print("=" * 40)
    
    try:
        start = int(input("Enter starting number (default 1): ") or "1")
        end = int(input("Enter ending number (default 50): ") or "50")
        
        if start > end:
            print("Error: Starting number cannot be greater than ending number.")
            return
        
        total = 0
        print(f"\nCalculating sum from {start} to {end}...")
        
        # Using for loop
        for number in range(start, end + 1):
            total += number
        
        print(f"\nThe sum of numbers from {start} to {end} is: {total}")
        
        # Using formula
        n = end - start + 1
        formula_sum = n * (start + end) // 2
        print(f"Verification using formula: {formula_sum}")
        
        if total == formula_sum:
            print("✓ Results verified!")
            
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    
    # Optional: Run advanced version
    run_advanced = input("\nDo you want to try with a custom range? (yes/no): ").strip().lower()
    if run_advanced in ['yes', 'y']:
        advanced_version()
    
    print("\nThank you for using the Sum Calculator!")
