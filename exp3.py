from XC3Tree import generate_xc3_tree

# print the heights of trees with degrees 0-25
for i in range(26):
    new_tree = generate_xc3_tree(i)
    print(f'degree{i:< 4} height:{new_tree.height()}')
