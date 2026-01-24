lst = [12, 3, 4, 10]

if len(lst) <= 1:
    result = lst
else:
    result = [lst[-1]] + lst[:-1]

print(result)