def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s


    length = len(s)
    for i in range(length // 2):
        print(s[length - i - 1])
        if s[i] != s[length - i - 1]:
            return False
    return True

# Використання функції
print(is_palindrome("Козак з 1казок"))  # Виведе: True