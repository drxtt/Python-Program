import re

def match_a_followed_by_b(string):
    pattern = r'^a.*b$'
    if re.match(pattern, string):
        return "The string matches the pattern."
    else:
        return "The string does not match the pattern."

def extract_4_digit_number(string):
    pattern = r'\\b\\d{4}\\b'
    match = re.findall(pattern, string)
    if match:
        return f"Found 4-digit number(s): {', '.join(match)}"
    else:
        return "No 4-digit number found in the string."

def convert_date_format(date_string):
    pattern = r'^(\\d{4})-(\\d{2})-(\\d{2})$'
    match = re.match(pattern, date_string)
    if match:
        return f"Converted date: {match.group(3)}-{match.group(2)}-{match.group(1)}"
    else:
        return "Invalid date format. Please use yyyy-mm-dd."

def find_five_char_words(string):
    pattern = r'\\b\\w{5}\\b'
    matches = re.findall(pattern, string)
    if matches:
        return f"Five-character words found: {', '.join(matches)}"
    else:
        return "No five-character words found."

def split_with_multiple_delimiters(string):
    pattern = r'[;,.\\s]'
    result = re.split(pattern, string)
    return f"Split result: {', '.join(filter(None, result))}"

def main():
    while True:
        print("\\nMenu:")
        print("1. Check if string matches 'a' followed by anything, ending in 'b'")
        print("2. Extract 4-digit number from a string")
        print("3. Convert date from yyyy-mm-dd to dd-mm-yyyy")
        print("4. Find all five-character long words in a string")
        print("5. Split a string with multiple delimiters")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            string = input("Enter the string: ")
            print(match_a_followed_by_b(string))
        elif choice == '2':
            string = input("Enter the string: ")
            print(extract_4_digit_number(string))
        elif choice == '3':
            date_string = input("Enter the date in yyyy-mm-dd format: ")
            print(convert_date_format(date_string))
        elif choice == '4':
            string = input("Enter the string: ")
            print(find_five_char_words(string))
        elif choice == '5':
            string = input("Enter the string: ")
            print(split_with_multiple_delimiters(string))
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
