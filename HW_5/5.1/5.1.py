import string
import keyword

name = input("Enter variable name: ")

def is_valid_variable(name):
    if not name:
        return False

    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    allowed = string.ascii_lowercase + string.digits + "_"
    for ch in name:
        if ch not in allowed:
            return False

    if set(name) == {"_"} and len(name) > 1:
        return False

    return True


print(is_valid_variable(name))
