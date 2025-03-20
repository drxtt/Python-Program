def reverse_string(s):
    return s[::-1]

def length_of_string(s):
    return len(s)

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_case(s):
    uppercase = sum(1 for char in s if char.isupper())
    lowercase = sum(1 for char in s if char.islower())
    return uppercase, lowercase

def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

def main():
    while True:
        print("\nMenu:")
        print("1. Reverse the string")
        print("2. Length of the string")
        print("3. Number of vowels in the string")
        print("4. Number of uppercase and lowercase letters")
        print("5. New string without any duplicate characters")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 6:
            print("Exiting the program.")
            break
        
        string = input("Enter a string: ")
        
        if choice == 1:
            print(f"Reversed string: {reverse_string(string)}")
        elif choice == 2:
            print(f"Length of the string: {length_of_string(string)}")
        elif choice == 3:
            print(f"Number of vowels in the string: {count_vowels(string)}")
        elif choice == 4:
            uppercase, lowercase = count_case(string)
            print(f"Number of uppercase letters: {uppercase}")
            print(f"Number of lowercase letters: {lowercase}")
        elif choice == 5:
            print(f"New string without duplicates: {remove_duplicates(string)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
