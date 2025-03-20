def convert_date_format(date_string):
    """Converts a date from yyyy-mm-dd to dd-mm-yyyy format."""
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.fullmatch(pattern, date_string)
    if match:
        year, month, day = match.groups()
        return f"{day}-{month}-{year}"
    else:
        return "Invalid date format"

# Example
print(convert_date_format("2024-12-09"))  # 09-12-2024
print(convert_date_format("09-12-2024"))  # Invalid date format
