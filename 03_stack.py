#stack을 Node로 구현해보자
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None


def true():
    n = int(input())
    istrue = True
    cur =1
    stack = []
    ans = []

    for i in range(n):
        num = int(input())
        while cur <= num :
            stack.append(cur)
            ans.append('+')
            cur+=1
        if stack[-1] == num :
            stack.pop()
            ans.append('-')

        else:
            istrue = False

    if istrue:
        for i in ans:
            print(i)
        return
    else:
        print("NO")
true()
