from XC3Tree import generate_xc3_tree

# print the heights of trees with degrees 0-25
result = ''
for i in range(26):
    new_tree = generate_xc3_tree(i)
    result += f'degree:{i} height:{new_tree.height()}' + ', ' + ('\n' if i % 3 == 1 else '')

print(result)

