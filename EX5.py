def main():
    # Create the dictionary with numbers and their squared values till 10
    squared_dict = {i: i**2 for i in range(1, 11)}

    while True:
        print("\nMenu:")
        print("1. Create and Print the Dictionary with numbers and their squared values till 10")
        print("2. Print the sum of all values in the Dictionary")
        print("3. Ask a number from the user and Remove it from the Dictionary")
        print("4. Print all items in the dictionary whose values are above 50")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 5:
            print("Exiting the program.")
            break
        
        if choice == 1:
            # Print the dictionary
            print(f"Dictionary with numbers and their squared values till 10: {squared_dict}")
        
        elif choice == 2:
            # Print the sum of all values in the dictionary
            total_sum = sum(squared_dict.values())
            print(f"The sum of all values in the dictionary: {total_sum}")
        
        elif choice == 3:
            # Ask for a number from the user to remove
            num_to_remove = int(input("Enter a number to remove from the dictionary: "))
            if num_to_remove in squared_dict:
                del squared_dict[num_to_remove]
                print(f"Updated dictionary after removing {num_to_remove}: {squared_dict}")
            else:
                print(f"Number {num_to_remove} not found in the dictionary.")
        
        elif choice == 4:
            # Print all items whose values are above 50
            print("Items in the dictionary whose values are above 50:")
            for key, value in squared_dict.items():
                if value > 50:
                    print(f"{key}: {value}")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
