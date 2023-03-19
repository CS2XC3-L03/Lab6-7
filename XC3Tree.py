class XC3Tree:
    def __init__(self, children=None):
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def degree(self):
        return len(self.children)

    def height(self):
        if self.degree() == 0:
            return 0
        else:
            return 1 + max([child.height() for child in self.children])

    def num_nodes(self):
        return 1 + sum([child.num_nodes() for child in self.children])


def generate_xc3_tree(degree, memo={}):
    if degree in memo:
        return memo[degree]
    if not degree:
        return XC3Tree()
    else:
        children = []
        for i in range(degree):
            children.append(generate_xc3_tree(i - 1 if i > 1 else 0, memo))
        memo[degree] = XC3Tree(children)
        return memo[degree]
