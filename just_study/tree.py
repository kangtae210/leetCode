# 이진 트리

def print_tree(target):
    print(target)
    print_tree(target.left)
    print_tree(target.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    




root = Node(1)

root.left = Node(11)
root.right = Node(12)

root.left.left = Node(111)
root.left.right = Node(112)

root.right.left = Node(121)
root.right.right = Node(122)


