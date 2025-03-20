import this

def write_to_file():
    # Open the file with exclusive creation mode ('x' mode)
    with open('zen_of_python.txt', 'x') as file:
        # Write the Zen of Python into the file
        file.write(this.s)

def print_file_contents():
    # Read and print the contents of the file
    with open('zen_of_python.txt', 'r') as file:
        content = file.read()
        print("Contents of the file:")
        print(content)

def count_words():
    # Count the total number of words in the file
    with open('zen_of_python.txt', 'r') as file:
        content = file.read()
        words = content.split()  # Split the content into words
        print(f"Total number of words in the file: {len(words)}")

def capitalize_words():
    # Capitalize the first letter of every word in the file
    with open('zen_of_python.txt', 'r') as file:
        content = file.read()
    # Capitalize the first letter of each word
    capitalized_content = content.title()
    with open('zen_of_python.txt', 'w') as file:
        file.write(capitalized_content)
    print("First letter of every word in the file has been capitalized.")

def print_reverse_contents():
    # Print the contents of the file in reverse order
    with open('zen_of_python.txt', 'r') as file:
        content = file.read()
    print("Contents of the file in reverse order:")
    print(content[::-1])

def main():
    while True:
        print("\nMenu:")
        print("1. Create a file and write the Zen of Python into it")
        print("2. Print all the data in the file")
        print("3. Print total number of words in the file")
        print("4. Capitalize the first letter of every word in the file")
        print("5. Print the contents of the file in reverse order")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            try:
                write_to_file()
                print("File created and data written successfully.")
            except FileExistsError:
                print("File already exists.")
        
        elif choice == 2:
            print_file_contents()
        
        elif choice == 3:
            count_words()
        
        elif choice == 4:
            capitalize_words()
        
        elif choice == 5:
            print_reverse_contents()
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
