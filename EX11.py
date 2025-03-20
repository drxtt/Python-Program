def inverted_pyramid_of_numbers(n):
    for i in range(n, 0, -1):
        print(" ".join(str(x) for x in range(1, i + 1)))

def reverse_pyramid_of_numbers(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(x) for x in range(i, 0, -1)))

def unique_pyramid_pattern_of_digits(n):
    num = 1
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()

def pyramid_of_horizontal_tables(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(f"{i * j:3}", end=" ")
        print()

def downward_triangle_pattern_of_stars(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    while True:
        print("\nMenu:")
        print("1. Inverted Pyramid of Numbers")
        print("2. Reverse Pyramid of Numbers")
        print("3. Unique Pyramid Pattern of Digits")
        print("4. Pyramid of Horizontal Tables")
        print("5. Downward Triangle Pattern of Stars")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice in {'1', '2', '3', '4', '5'}:
            try:
                n = int(input("Enter the number of rows: "))
                if n <= 0:
                    print("Number of rows must be positive.")
                    continue
                if choice == '1':
                    inverted_pyramid_of_numbers(n)
                elif choice == '2':
                    reverse_pyramid_of_numbers(n)
                elif choice == '3':
                    unique_pyramid_pattern_of_digits(n)
                elif choice == '4':
                    pyramid_of_horizontal_tables(n)
                elif choice == '5':
                    downward_triangle_pattern_of_stars(n)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
