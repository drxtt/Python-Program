def read_numbers(file_path):
    """Reads numbers from a file and returns them as a list of integers."""
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip()
            return [int(num.strip()) for num in data.split(",") if num.strip().isdigit()]
    except Exception as e:
        print(f"Error reading numbers file: {e}")
        return []

def read_words(file_path):
    """Reads words from a file and returns them as a list of strings."""
    try:
        with open(file_path, 'r') as file:
            return [word.strip() for word in file.read().strip().split(",")]
    except Exception as e:
        print(f"Error reading words file: {e}")
        return []

def write_to_file(file_path, content):
    """Writes content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def calculate_sums(numbers):
    """Calculates the sum of odd and even numbers."""
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    sum_even = sum(num for num in numbers if num % 2 == 0)
    return sum_odd, sum_even

def generate_output(numbers, words):
    """Generates the final output by associating numbers with words."""
    output = []
    for i, num in enumerate(numbers):
        word = words[i % len(words)]  # Loop through words cyclically
        output.append(f"{num} {word}")
    return ", ".join(output)

def main():
    # File paths
    digits_file = "input_digits_P1.txt"
    words_file = "input_words_P1.txt"
    sum_odd_file = "sum_of_odd_numbers.txt"
    sum_even_file = "sum_of_even_numbers.txt"
    final_output_file = "final_output.txt"

    # Read data from files
    numbers = read_numbers(digits_file)
    words = read_words(words_file)

    if not numbers or not words:
        print("Error: Input files could not be read correctly. Exiting.")
        return

    # Calculate sums
    sum_odd, sum_even = calculate_sums(numbers)

    # Write sums to respective files
    write_to_file(sum_odd_file, str(sum_odd))
    write_to_file(sum_even_file, str(sum_even))

    # Generate final output
    final_output = generate_output(numbers, words)

    # Write final output to file
    write_to_file(final_output_file, final_output)

    print("Processing complete. Files generated:")
    print(f"1. Sum of odd numbers: {sum_odd_file}")
    print(f"2. Sum of even numbers: {sum_even_file}")
    print(f"3. Final output: {final_output_file}")

if __name__ == "__main__":
    main()
