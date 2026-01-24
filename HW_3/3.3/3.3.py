lst = [1, 2, 3, 4, 5]

n = len(lst)

if n == 0:
    result = [[], []]
else:
    mid = (n + 1) // 2
    result = [lst[:mid], lst[mid:]]

print(result)
