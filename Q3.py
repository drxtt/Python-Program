def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    if len(unique_lst) < 2:
        return "Not enough distinct numbers"
    return unique_lst[-2]

def swap_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def remove_duplicates(lst):
    return list(set(lst))

def odd_occurrence(lst):
    from collections import Counter
    counts = Counter(lst)
    return [num for num, count in counts.items() if count % 2 != 0]

def square_numbers(lst):
    return [x ** 2 for x in lst]

def main():
    while True:
        print("\nMenu:")
        print("1. Print the second largest number in the list")
        print("2. Swap the first and last items of the list")
        print("3. Remove duplicates from the list")
        print("4. Print numbers occurring an odd number of times")
        print("5. Print the list of squares of the numbers")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 6:
            print("Exiting the program.")
            break
        
        # Input the list from the user
        user_input = input("Enter a list of numbers (comma-separated): ")
        lst = [int(x.strip()) for x in user_input.split(',')]

        if choice == 1:
            print(f"Second largest number: {second_largest(lst)}")
        elif choice == 2:
            print(f"List after swapping first and last items: {swap_first_last(lst)}")
        elif choice == 3:
            print(f"List after removing duplicates: {remove_duplicates(lst)}")
        elif choice == 4:
            print(f"Numbers occurring odd number of times: {odd_occurrence(lst)}")
        elif choice == 5:
            print(f"List of squares: {square_numbers(lst)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
