class InvalidAgeException(Exception):
    def __init__(self, age, message="Age must be above 18 and below 100."):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age <= 18 or age >= 100:
        raise InvalidAgeException(age)
    return f"Age {age} is valid."

# Main program
def main():
    try:
        age = int(input("Enter your age: "))
        print(check_age(age))
    except InvalidAgeException as e:
        print(f"InvalidAgeException: {e.message} (Provided: {e.age})")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
