def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def is_prime(n, divisor=None):
    if divisor is None:
        divisor = n - 1
    if n <= 1:
        return False
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

def main():
    while True:
        print("\nMenu:")
        print("1. Print Fibonacci Series up to the number")
        print("2. Print Factorial of the number")
        print("3. Print the Sum of the digits in the number")
        print("4. Check if the number is Prime or Not")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting the program.")
            break
        
        # Taking user input for the number
        number = int(input("Enter a number: "))

        if choice == 1:
            print("Fibonacci Series up to", number, ": ", end="")
            for i in range(number):
                print(fibonacci(i), end=" ")
            print()  # For new line after the series
        
        elif choice == 2:
            print(f"Factorial of {number} is: {factorial(number)}")
        
        elif choice == 3:
            print(f"Sum of digits of {number} is: {sum_of_digits(number)}")
        
        elif choice == 4:
            if is_prime(number, number - 1):
                print(f"{number} is a Prime Number.")
            else:
                print(f"{number} is not a Prime Number.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
