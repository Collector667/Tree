class node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.lch = None
        self.rch = None
        self.parent = None

class Tree:
    def __init__(self):
        self.Root = None
    def insert(self, newNode):
        x = self.Root
        y = None
        while (x is not None):
            y = x
            if newNode.key < x.key:
                x = x.lch
            else:
                x = x.rch
        newNode.parent = y
        if y is None:
            self.Root = newNode
        elif newNode.key < y.key:
            y.lch = newNode
        else:
            y.rch = newNode
    def search(self, key):
        x = self.Root
        while (x is not None and x.key != key):
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
    def delete(self, key):
        z = self.search(key)
        if z is None:
            return
        else:
            if z.lch is None:
                self.Transplant(z, z.rch)
            elif z.rch is None:
                self.Transplant(z, z.lch)
            else:
                y = self.Treemin(z.rch)
                if y is not z.rch:
                    self.Transplant(y, y.rch)
                    y.rch = z.rch
                    y.rch.parent = y
                self.Transplant(z, y)
                y.lch = z.lch
                y.lch.parent = y

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




