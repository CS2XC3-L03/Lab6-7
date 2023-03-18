class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() is None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        new_parent = self.left
        if new_parent is None:
            return
        self.left = new_parent.right
        if self.left is not None:
            self.left.parent = self
        new_parent.right = self
        new_parent.parent = self.parent
        if self.parent is not None:
            if self.is_left_child():
                self.parent.left = new_parent
            else:
                self.parent.right = new_parent
        self.parent = new_parent

    def rotate_left(self):
        new_parent = self.right
        if new_parent is None:
            return
        self.right = new_parent.left
        if self.right is not None:
            self.right.parent = self
        new_parent.left = self
        new_parent.parent = self.parent
        if self.parent is not None:
            if self.is_left_child():
                self.parent.left = new_parent
            else:
                self.parent.right = new_parent
        self.parent = new_parent


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right is None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        if node.parent is None:
            node.make_black()
            return
        while node is not self.root and node.parent.is_red():
            if node.parent.is_left_child():
                uncle = node.get_uncle()
                if uncle is not None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_right_child():
                        node = node.parent
                        node.rotate_left()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_right()
            else:
                uncle = node.get_uncle()
                if uncle is not None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_left_child():
                        node = node.parent
                        node.rotate_right()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_left()
        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left is None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right is None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

    def find(self, k):
        current_node = self.root
        while current_node is not None:
            if current_node.value < k:
                current_node = current_node.right
            elif current_node.value > k:
                current_node = current_node.left
            else:
                return current_node
        return None

    def black_path_length(self, node):
        count = 0
        current_node = node
        while current_node is not None:
            if current_node.is_black():
                count += 1
            current_node = current_node.parent
        return count

    def is_valid(self, values):
        black_length = None
        for value in values:
            node = self.find(value)
            if node.is_leaf():
                if black_length is None:
                    black_length = self.black_path_length(node)
                elif self.black_path_length(node) != black_length:
                    print("Not valid (number of black lengths not consistent)")
                    return False
            if node.parent is not None and node.is_red() and node.parent.is_red():
                print("Not valid (two red links in a row)")
                return False
            if node.is_red() and node.is_right_child():
                print("Not valid (right-leaning red link)")
                return False
        return True
