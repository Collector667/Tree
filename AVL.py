class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.lch = None
        self.rch = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.lch) - self.height(node.rch)

    def insert(self, node, key):

        if not node:
            return Node(key)
        elif key < node.key:
            node.lch = self.insert(node.lch, key)
        else:
            node.rch = self.insert(node.rch, key)

        node.height = 1 + max(self.height(node.lch), self.height(node.rch))
        balance = self.balance(node)

        #Малые повороты
        if balance > 1 and key < node.lch.key:
            return self.right_rot(node)


        if balance < -1 and key > node.rch.key:
            return self.left_rot(node)

        #Большие повороты
        if balance > 1 and key > node.lch.key:
            node.lch = self.left_rot(node.lch)
            return self.right_rot(node)

        # Right-Left rotation
        if balance < -1 and key < node.rch.key:
            node.rch = self.right_rot(node.rch)
            return self.left_rot(node)

        return node

    def delete(self, node, key):
        if not node:
            return node

        if key < node.value:
            node.lch = self.delete(node.lch, key)
        elif key > node.key:
            node.rch = self.delete(node.rch, key)
        else:
            if not node.lch:
                temp = node.rch
                node = None
                return temp
            elif not node.rch:
                temp = node.lch
                node = None
                return temp

            temp = self.min_node(node.rch)
            node.value = temp.value
            node.rch = self.delete(node.rch, temp.value)

        if not node:
            return node

        node.height = 1 + max(self.height(node.lch), self.height(node.rch))
        balance = self.balance(node)

        #Малые повороты
        if balance > 1 and self.balance(node.lch) >= 0:
            return self.right_rot(node)


        if balance < -1 and self.balance(node.rch) <= 0:
            return self.left_rot(node)

        #Большие повороты
        if balance > 1 and self.balance(node.lch) < 0:
            node.lch = self.left_rot(node.lch)
            return self.right_rot(node)


        if balance < -1 and self.balance(node.rch) > 0:
            node.rch = self.right_rot(node.rch)
            return self.left_rot(node)

        return node

    def left_rot(self, z):
        y = z.rch
        x = y.lch

        y.lch = z
        z.rch = x

        z.height = 1 + max(self.height(z.lch), self.height(z.rch))
        y.height = 1 + max(self.height(y.lch), self.height(y.rch))

        return y

    def right_rot(self, z):
        y = z.lch
        x = y.rch

        y.rch = z
        z.lch = x

        z.height = 1 + max(self.height(z.lch), self.height(z.rch))
        y.height = 1 + max(self.height(y.lch), self.height(y.rch))

        return y

    def min_node(self, root):
        current = root
        while current.lch:
            current = current.lch
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.rch, value)
        return self.search(root.lch, value)

    def insert_node(self, newNode):
        self.root = self.insert(self.root, newNode.key)

    def delete_node(self, key):
        self.root = self.delete(self.root, key)
    def depth_traversal(self, node, keys, mode):
        if node:
            if mode.upper() == "NLR":
                keys.append(node.key)
                self.depth_traversal(node.lch, keys, mode)
                self.depth_traversal(node.rch, keys, mode)
            elif mode.upper() == "LNR":
                self.depth_traversal(node.lch, keys, mode)
                keys.append(node.key)
                self.depth_traversal(node.rch, keys, mode)
            else:
                self.depth_traversal(node.lch, keys, mode)
                self.depth_traversal(node.rch, keys, mode)
                keys.append(node.key)
        return keys
    def breadth_traversal(self):
        listOfkeys = []
        level = [self.root]
        len_level = 1
        while len(level) != 0:
            levelKeys = []
            for i in range(len(level)):
                levelKeys.append(level[i].key)
                if level[i].lch:
                    level.append(level[i].lch)
                if level[i].rch:
                    level.append(level[i].rch)

            listOfkeys.append(levelKeys)
            level = level[len_level:]
            len_level = len(level)
        return listOfkeys




tree = AVLTree()

for i in range(8, 0, -1):
    k = Node(i)
    tree.insert_node(k)
keys = []
print(tree.depth_traversal(tree.root, keys, "NLR"))
keys = tree.breadth_traversal()

for i in range(len(keys)):
    print(keys[i])


