def main():
    while True:
        print("\nMenu:")
        print("1. Print the Union of the Lists")
        print("2. Print the Intersection of the Lists")
        print("3. Print the Merged and Sorted List")
        print("4. Print the sum of all the numbers in both lists")
        print("5. Print the average of all the numbers in both lists")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 6:
            print("Exiting the program.")
            break
        
        # Input the two lists from the user
        user_input1 = input("Enter the first list of numbers (comma-separated): ")
        list1 = [int(x.strip()) for x in user_input1.split(',')]
        
        user_input2 = input("Enter the second list of numbers (comma-separated): ")
        list2 = [int(x.strip()) for x in user_input2.split(',')]

        if choice == 1:
            # Union of the lists
            union = list(set(list1) | set(list2))
            print(f"Union of the lists: {union}")

        elif choice == 2:
            # Intersection of the lists
            intersection = list(set(list1) & set(list2))
            print(f"Intersection of the lists: {intersection}")

        elif choice == 3:
            # Merged and sorted list
            merged_sorted = sorted(list1 + list2)
            print(f"Merged and sorted list: {merged_sorted}")

        elif choice == 4:
            # Sum of all numbers in both lists
            total_sum = sum(list1) + sum(list2)
            print(f"Sum of all numbers in both lists: {total_sum}")

        elif choice == 5:
            # Average of all numbers in both lists
            total_count = len(list1) + len(list2)
            if total_count > 0:
                average = (sum(list1) + sum(list2)) / total_count
                print(f"Average of all numbers in both lists: {average}")
            else:
                print("The lists are empty, so the average cannot be calculated.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
