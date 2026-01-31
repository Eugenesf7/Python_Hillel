import string
import keyword

name = input("Enter variable name: ")

def is_valid_variable(name):
    # 1. Should not be empty
    if not name:
        return False

    # 2. Should not be a reserved word
    if name in keyword.kwlist:
        return False

    # 3. Should not start with a number
    if name[0].isdigit():
        return False

    # 4. Only lowercase letters, numbers and _
    allowed = string.ascii_lowercase + string.digits + "_"
    for ch in name:
        if ch not in allowed:
            return False

    # 5. No more than one _
    if name.count("_") > 1:
        return False

    return True


print(is_valid_variable(name))