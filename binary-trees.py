import random

class TreeNode:
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = None

    # Insert
    def insert(self, data):
        new_node = TreeNode(data)
        # Special Case: Empty tree
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            inserted = False
            while not inserted:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new_node
                        inserted = True
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new_node
                        inserted = True

    def height(self):
        return self.node_height(self.head)

    def node_height(self, current):
        if current == None:
            return 0
        if current.left == None and current.right == None:
            return 1
        else:
            return 1 + max([self.node_height(current.left), self.node_height(current.right)])

    def size(self):
        return self.node_size(self.head)
    
    def node_size(self, current):
        if current:
            return 1 + self.node_size(current.left) + self.node_size(current.right)
        else:
            return 0

    def traverse(self, style):
        if style == 'inorder':
            return self.in_order_traversal(self.head)
        elif style == 'preorder':
            return self.pre_order_traversal(self.head)
        elif style == 'postorder':
            return self.post_order_traversal(self.head)
        else:
            print("Don't know what to do. Options are 'inorder', 'preorder', or 'postorder'")

    def in_order_traversal(self, current):
        if current:
            return list(self.in_order_traversal(current.left)) + [current.data] + list(self.in_order_traversal(current.right))
        else:
            return []
    
    def pre_order_traversal(self, current):
        if current:
            return list(self.pre_order_traversal(current.left)) + list(self.pre_order_traversal(current.right)) + [current.data]
        else:
            return []

    def post_order_traversal(self, current):
        if current:
            return [current.data] + list(self.post_order_traversal(current.left)) + list(self.post_order_traversal(current.right))
        else:
            return []

input_list = []
for i in range(10):
    input_list.append(i)
random.shuffle(input_list)

my_tree = BinaryTree()
for i in input_list:
    # print('item:', i)
    my_tree.insert(int(i))

print(my_tree.traverse('inorder'))
print(my_tree.traverse('preorder'))
print(my_tree.traverse('postorder'))

print('Height:', my_tree.height())
print('Size', my_tree.size())