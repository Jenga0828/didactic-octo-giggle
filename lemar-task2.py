# Function to check if a number is divisible by 3
def is_divisible_by_3(number):
    return number % 3 == 0

# Main function
def main():
    # Prompt the user to enter a number
    number = int(input("Enter a number: "))
    
    # Check if the number is divisible by 3
    if is_divisible_by_3(number):
        print(f"{number} is divisible by 3.")
    else:
        print(f"{number} is not divisible by 3.")

# Run the main function
if __name__ == "__main__":
    main()
