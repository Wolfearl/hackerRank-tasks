class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    if v1 > v2:
        v2, v1 = v1, v2
    current = root
    while current:
        if current.info > v2:
            current = current.left
        elif current.info < v1:
            current = current.right
        else:
            return current


tree = BinarySearchTree()
t = 6

arr = [4, 2, 3, 1, 7, 6]

for i in range(t):
    tree.create(arr[i])

v = 1, 7

ans = lca(tree.root, v[0], v[1])
print(ans.info)