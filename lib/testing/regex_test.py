import re

# Regular expression patterns
name_pattern = r"^[A-Za-z]+(?: [A-Za-z]+)?$"  # Allows for first name and optional last name
phone_number_pattern = r"^\d{3}-\d{3}-\d{4}$"  # Matches xxx-xxx-xxxx format
email_address_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # Matches email address format

# Compile regular expressions
name_regex = re.compile(name_pattern)
phone_regex = re.compile(phone_number_pattern)
email_regex = re.compile(email_address_pattern)
