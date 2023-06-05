import re

def check_password_strength(password):
    # Перевірка довжини паролю
    if len(password) < 8:
        return "Пароль має містити принаймні 8 символів"

    # Перевірка використання великих та малих літер
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return "Пароль має містити як малі, так і великі літери"

    # Перевірка використання цифр
    if not re.search(r"\d", password):
        return "Пароль має містити принаймні одну цифру"

    # Перевірка використання спеціальних символів
    if not re.search(r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]", password):
        return "Пароль має містити принаймні один спеціальний символ"

    return "Пароль має достатню потужність"

# Приклад використання
password = input("Введіть пароль для перевірки: ")
result = check_password_strength(password)
print(result)
