import collections
from collections import deque
#두 이진 트리 병합
#617.Merge Two Binary Trees
class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left =left
        self.right = right

def MergeTrees(t1:TreeNode, t2:TreeNode):
    if t1 and t2:
        node = TreeNode(t1.value + t2.value)
        node.left = MergeTrees(t1.left, t2.left)
        node.right = MergeTrees(t1.right, t2.right)

        return node
    else:
        return t1 or t2



t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.right.right = TreeNode(5)
t1.right.left = TreeNode(4)

t2 = TreeNode(2)
t2.left=  TreeNode(1)
t2.right =TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

# print(MergeTrees(t1,t2))

class Codec:

    def serialize(self, root):

        q = collections.deque()
        string = []
        if not root:
            return ""
        q.append(root)
        while q:
            cur = q.popleft()
            if cur.val is None:
                string.append("#")
            else:
                if not cur.left:
                    q.append(TreeNode(None))
                if cur.left:
                    q.append(cur.left)
                if not cur.right:
                    q.append(TreeNode(None))
                if cur.right:
                    q.append(cur.right)
                string.append(str(cur.val))
        while string[-1] == "#":
            string.pop()

        return ' '.join(string)

    def deserialize(self, data):
        if len(data) == 0:
            return

        datas = data.split()
        for i in range(len(datas)):
            if datas[i] == "#":
                datas[i] = "null"

        q = collections.deque(datas)
        nodequeue = collections.deque()
        root = TreeNode(q.popleft())
        nodequeue.append(root)
        while q:
            node = nodequeue.popleft()
            node.left = TreeNode(q.popleft())
            nodequeue.append(node.left)
            if q:
                node.right = TreeNode(q.popleft())
                nodequeue.append(node.right)

        return root


dec = Codec()
deser = Codec()
print(deser.deserialize(dec.serialize(t2)))
print(dec.serialize(t2))

