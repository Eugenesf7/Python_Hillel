lst = [0, 1, 0, 12, 3]

non_zero = [x for x in lst if x != 0]

zero = [0] * (len(lst) - len(non_zero))

result = non_zero + zero
ч
print(result)