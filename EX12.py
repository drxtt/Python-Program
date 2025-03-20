def reverse_each_word(sentence):
    """Reverses each word in a sentence."""
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def sort_by_word_length_with_count(string):
    """Sorts words by length and appends the count of characters to each word."""
    words = string.split()
    sorted_words = sorted(words, key=len)
    return " ".join([f"{word}({len(word)})" for word in sorted_words])

def string_to_integer(number_string):
    """Converts a string to an integer without using inbuilt functions."""
    num = 0
    for char in number_string:
        if '0' <= char <= '9':
            num = num * 10 + (ord(char) - ord('0'))
        else:
            return "Invalid number string."
    return num

def append_character_count(string):
    """Appends the count of each character to itself in the string (ignoring case)."""
    lower_string = string.lower()
    result = ""
    for char in string:
        if char.isalpha():
            count = lower_string.count(char.lower())
            result += f"{char}{count}"
        else:
            result += char
    return result

def main():
    while True:
        print("\nMenu:")
        print("1. Reverse each word in a sentence")
        print("2. Sort words by length and append word lengths")
        print("3. Convert a number (string) into an integer without inbuilt functions")
        print("4. Append character count after each character in a string")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            sentence = input("Enter a sentence: ")
            print("Reversed Sentence:", reverse_each_word(sentence))
        elif choice == '2':
            string = input("Enter a string: ")
            print("Sorted Words with Counts:", sort_by_word_length_with_count(string))
        elif choice == '3':
            number_string = input("Enter a number as a string: ")
            result = string_to_integer(number_string)
            print(f"Converted Integer: {result}" if isinstance(result, int) else result)
        elif choice == '4':
            string = input("Enter a string: ")
            print("Appended Character Count:", append_character_count(string))
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
