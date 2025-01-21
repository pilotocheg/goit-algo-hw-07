class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value(root.right)
        root.right = delete(root.right, root.val)
    return root


# task 1
def max_value(node):
    if not node.right:
        return node.val

    return max_value(node.right)


# task 2
def min_value(node):
    if not node.left:
        return node.val

    return min_value(node.left)


# task 3
def sum(node):
    if not node:
        return 0

    return node.val + sum(node.left) + sum(node.right)


def test():
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    assert max_value(root) == 8
    assert min_value(root) == 2
    assert sum(root) == 35

    root = insert(root, 5)

    assert max_value(root) == 8
    assert min_value(root) == 2
    assert sum(root) == 40

    root = delete(root, 2)
    root = delete(root, 8)

    assert max_value(root) == 7
    assert min_value(root) == 3
    assert sum(root) == 30


if __name__ == "__main__":
    test()
