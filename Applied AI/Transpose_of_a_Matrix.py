Matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# transposed = []
# Using List Comprehension
transposed = [[row[i] for row in Matrix] for i in range(4)]

# for i in range(4):
#     lst = []
#     for row in Matrix:
#         lst.append(row[i])
#     transposed.append(lst)

print(transposed)

# Wrong Method
# lst = []
# for i in range(4):
#     for row in Matrix:
#         lst.append(row[i])
#     transposed.append(lst)
#     lst.clear()
