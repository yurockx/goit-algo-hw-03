import re
def normalize_phone(phone_number):
    full_prefix = "+38"
    short_prefix = "+"
    pattern = r"[^0-9+]"
    replacement = ""
    numbers_only = re.sub(pattern, replacement, phone_number)
    if numbers_only.startswith("0"):
        return str(full_prefix + numbers_only)
    elif numbers_only.startswith("38"):
        return str(short_prefix + numbers_only)
    else:
        return str(numbers_only)

