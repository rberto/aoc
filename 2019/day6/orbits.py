class Node():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.childs = []

    def addchild(self, child):
        childs.append(child)

    def disttoroot(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.disttoroot() + 1


    def disttoparent(self, name):
        if self.parent.name == name:
            return 0
        else:
            return self.parent.disttoparent(name) + 1

    def listparents(self, l):
        if self.parent == None:
            l.append(self.name)
            return l
        else:
            l.append(self.name)
            self.parent.listparents(l)


def firstcommonelt(l1, l2):
    for e in l1:
        if e in l2:
            return e
    return None
            
root = Node("COM", None)

node1 = Node("ded", root)

node2 = Node("ede", node1)

print(node2.disttoroot())

nodes = {}

with open("./input", "r") as f:
    for line in f.readlines():
        parentname = line.split(')')[0].strip()
        childname = line.split(')')[1].strip()
        if parentname not in nodes:
            print("New node:", parentname)
            nodes[parentname] = Node(parentname, None)
        else:
            print("here")
        if childname not in nodes:
            print("New node:", childname)
            nodes[childname] = Node(childname, nodes[parentname])
        elif nodes[childname].parent == None:
            print("Setting", childname, "to", parentname)
            nodes[childname].parent = nodes[parentname]

l1=[]
l2=[]
nodes["YOU"].listparents(l1)
nodes["SAN"].listparents(l2)

l1.remove("COM")
l2.remove("COM")
print(l1)

common = firstcommonelt(l1, l2)
print(common)
print(nodes["YOU"].disttoparent(common) + nodes["SAN"].disttoparent(common))
print()
