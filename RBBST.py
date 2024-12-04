Red = 1
Black = 0

class NilNode:
    key = None
    color = Black
    lch = None
    rch = None

class RBnode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.lch = None
        self.rch = None
        self.parent = None
        self.color = Red

class RBTree:
    def __init__(self):
        self.Nil = NilNode
        self.Root = self.Nil

    def leftRot(self, node):
        y = node.rch
        node.rch = y.rch
        if y.lch != self.Nil:
            y.lch.parent = node
        y.p = node.parent
        if node.parent == self.Nil:
            self.Root = node
        elif node == node.parent.lch:
            node.parent.lch = y
        else:
            node.parent.rch = y
        y.lch = node
        node.parent = y


    def rightRot(self, node):
        y = node.lch
        node.lch = y.lch
        if y.rch != self.Nil:
            y.rch.parent = node
        y.parent = node.parent
        if node.parent == self.Nil:
            self.Root = node
        elif node == node.parent.lch:
            node.parent.lch = y
        else:
            node.parent.rch = y
        y.rch = node
        node.parent = y

    def Fixup(self, node):
        while node.parent.color == Red:
            if node.parent == node.parent.parent.lch:
                y = node.parent.parent.rch
                if y.color == Red: #case 1
                    node.parent.color = Black
                    y.color = Red
                    node = node.parent.parent
                else:
                    if node == node.parent.rch: #case 2
                        node = node.parent
                        self.leftRot(node)
                    node.parent.color = Black #case 3
                    node.parent.parent.color = Red
                    self.rightRot(node.parent.parent)
            else: #зеркально
                y = node.parent.parent.lch
                if y.color == Red:
                    node.parent.color = Black
                    y.color = Black
                    node.parent.parent.color = Red
                    node = node.parent.parent
                else:
                    if node == node.parent.lch:
                        node = node.parent
                        self.rightRot(node)
                    node.parent.color = Black
                    node.parent.parent.color = Red
                    self.leftRot(node.parent.parent)
        while node.parent != self.Nil:
            node = node.parent
        self.Root = node
        self.Root.color = Black

    def insert(self, newNode):
        x = self.Root
        y = self.Nil
        while x != self.Nil:
            y = x
            if newNode.key < x.key:
                x = x.lch
            else:
                x = x.rch
        newNode.parent = y
        if y is self.Nil:
            self.Root = newNode
        elif newNode.key < y.key:
            y.lch = newNode
        else:
            y.rch = newNode
        newNode.lch = self.Nil
        newNode.rch = self.Nil
        newNode.color = Red
        self.Fixup(newNode)
    def search(self, key):
        x = self.Root
        while x is not self.Nil and x.key != key:
            if key < x.key:
                x = x.lch
            else:
                x = x.rch
        return x
    def Transplant(self, node1, node2):
        if node1.parent is None:
            self.Root = node2
        elif node1 == node1.parent.lch:
            node1.parent.lch = node2
        else:
            node1.parent.rch = node2
        if node2 is not None:
            node2.parent = node1.parent
    def Treemin(self, node):
        x = node
        while x.lch is not None:
            x = x.lch
        return x
    def delFixup(self, node):
        while node != self.Root and node.color == Black:
            if node.parent.lch == node:
                w = node.parent.rch
                if w.color == Red:
                    w.color = Black
                    node.parent.color = Red
                    self.leftRot(node.parent)
                    w = node.parent.rch
                if w.lch.color== Black and w.rch.color ==Black:
                    w.color = Red
                    node = node.parent
                else:
                    if w.rch.color == Black:
                        w.lch.color = Black
                        w.color = Red
                        self.rightRot(w)
                        w = node.parent.rch
                    w.color = node.parent.color
                    node.parent.color = Black
                    w.rch.color = Black
                    self.leftRot(node.parent)
                    node = self.Root
            else:
                if node.parent.lch == node:
                    w = node.parent.rch
                    if w.color == Red:
                        w.color = Black
                        node.parent.color = Red
                        self.leftRot(node.parent)
                        w = node.parent.rch
                    if w.lch.color == Black and w.rch.color == Black:
                        w.color = Red
                        node = node.parent
                    else:
                        if w.rch.color == Black:
                            w.lch.color = Black
                            w.color = Red
                            self.rightRot(w)
                            w = node.parent.rch
                        w.color = node.parent.color
                        node.parent.color = Black
                        w.rch.color = Black
                        self.leftRot(node.parent)
                        node = self.Root
                else:
                    w = node.parent.lch
                    if w.color == Red:
                        w.color = Black
                        node.parent.color = Red
                        self.rightRot(node.parent)
                        w = node.parent.lch
                    if w.rch.color == Black and w.lch.color == Black:
                        w.color = Red
                        node = node.parent
                    else:
                        if w.lch.color == Black:
                            w.rch.color = Black
                            w.color = Red
                            self.leftRot(w)
                            w = node.parent.lch
                        w.color = node.parent.color
                        node.parent.color = Black
                        w.lch.color = Black
                        self.rightRot(node.parent)
                        node = self.Root

    def delete(self, key):
        z = self.search(key)
        originalColor = z.color
        if z.lch == self.Nil:
            x = z.rch
            self.Transplant(z, z.rch)
        elif z.rch == self.Nil:
            x = z.lch
            self.Transplant(z, z.lch)
        else:
            y = self.Treemin(z.rch)
            originalColor = y.color
            x = y.rch
            if y != z.rch:
                self.Transplant(y, y.rch)
                y.rch = z.rch
                y.rch.parent = y
            else:
                x.parent = y
            self.Transplant(z, y)
            y.lch = z.lch
            y.lch.parent = y
            y.color = z.color
        if originalColor == Black:
            self.delFixup(x)
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
        level = [self.Root]
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

tree = RBTree()
for i in range(8, 0, -1):
    k = RBnode(i)
    tree.insert(k)
keys = []
print(tree.depth_traversal(tree.Root, keys, "NLR"))
keys = tree.breadth_traversal()

for i in range(len(keys)):
    print(keys[i])






