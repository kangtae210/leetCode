# 이진 트리

def print_tree(target):
    if target:
        print(target.data)
        print_tree(target.left)
        print_tree(target.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def remove_left(self):
        self.left = None

    def remove_right(self):
        self.right = None
    
    def insert_left(self, new):
        self.left = new
    def insert_right(self, new):
        self.right = new        
    

root = Node(1)

root.insert_left(Node(11))
root.insert_right(Node(13))
root.insert_right(Node(12))


sample = Node(35)
sample.insert_left(Node(27))
sample.insert_right(Node(13))

root.left.insert_left(sample)


print_tree(root)