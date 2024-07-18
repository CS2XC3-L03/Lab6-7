from XC3Tree import generate_xc3_tree

# print the number of nodes in trees with degrees 0-25
result = ''
for i in range(26):
    new_tree = generate_xc3_tree(i)
    result += f'degree:{i} #nodes:{new_tree.num_nodes()}' + ', ' + ('\n' if i % 3 == 1 else '')

print(result)
