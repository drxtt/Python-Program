def reverse_number(n):
    return int(str(n)[::-1])

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def print_series(n):
    return " + ".join(str(i) for i in range(1, n+1)) + " = " + str(sum(range(1, n+1)))

def smallest_divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i
    return n  # If no divisor found, the number itself is prime and its smallest divisor is itself

def main():
    while True:
        print("\nMenu:")
        print("1. Reverse of the given number")
        print("2. Sum of Digits")
        print("3. Palindrome or Not")
        print("4. Series '1 + 2 + ... + n'")
        print("5. Smallest Divisor of the given number")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 6:
            print("Exiting the program.")
            break
        
        number = int(input("Enter a number: "))
        
        if choice == 1:
            print(f"Reverse of the number: {reverse_number(number)}")
        elif choice == 2:
            print(f"Sum of digits: {sum_of_digits(number)}")
        elif choice == 3:
            if is_palindrome(number):
                print(f"{number} is a Palindrome")
            else:
                print(f"{number} is not a Palindrome")
        elif choice == 4:
            print(f"Series: {print_series(number)}")
        elif choice == 5:
            print(f"Smallest divisor of {number} is: {smallest_divisor(number)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
