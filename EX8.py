from datetime import datetime, timedelta

def print_current_datetime():
    # Get current date and time
    now = datetime.now()
    # Format the date and time
    formatted_datetime = now.strftime("%d-%m-%Y %I:%M:%S %p")
    print(f"Current Date and Time: {formatted_datetime}")

def print_all_sundays(year):
    # Find all Sundays of the specified year
    sundays = []
    date = datetime(year, 1, 1)
    # Loop through the year to find all Sundays
    while date.year == year:
        if date.weekday() == 6:  # Sunday is 6
            sundays.append(date.strftime("%d-%m-%Y"))
        date += timedelta(days=1)
    print(f"All Sundays in {year}:")
    for sunday in sundays:
        print(sunday)

def add_28_days():
    # Get current date
    now = datetime.now()
    # Add 28 days
    new_date = now + timedelta(days=28)
    print(f"New Date after adding 28 days: {new_date.strftime('%d-%m-%Y')}")

def print_day_of_given_date():
    # Get a date from user input
    date_input = input("Enter a date (DD-MM-YYYY): ")
    try:
        date_object = datetime.strptime(date_input, "%d-%m-%Y")
        day_of_week = date_object.strftime("%A")
        print(f"The day of the week for {date_input} is: {day_of_week}")
    except ValueError:
        print("Invalid date format! Please enter in DD-MM-YYYY format.")

def calculate_age():
    # Get Date of Birth from user input
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
    try:
        dob = datetime.strptime(dob_input, "%d-%m-%Y")
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format! Please enter in DD-MM-YYYY format.")

def main():
    while True:
        print("\nMenu:")
        print("1. Print the current Date and Time")
        print("2. Print all the Sundays of a specified year")
        print("3. Print new Date after adding 28 days to the current Date")
        print("4. Print the Day of the given Date")
        print("5. Calculate Age by taking Date of Birth")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_current_datetime()
        elif choice == 2:
            year = int(input("Enter the year: "))
            print_all_sundays(year)
        elif choice == 3:
            add_28_days()
        elif choice == 4:
            print_day_of_given_date()
        elif choice == 5:
            calculate_age()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
