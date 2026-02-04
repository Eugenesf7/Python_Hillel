import string

letters = string.ascii_letters

s = input("Enter two letters with a hyphen: ")

start, end = s.split("-")

i1 = letters.index(start)
i2 = letters.index(end)

result = letters[i1:i2+1]

print(result)
