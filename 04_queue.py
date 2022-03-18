#Node 구현
import collections
from collections import deque


class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

#Node를 이용해서 Queue구현
class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None

#N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
#1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
#이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
#우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
#N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

def test_problem_queue(num):
    # 문제 https://www.acmicpc.net/problem/2164
    # 빠른이유 https://wiki.python.org/moin/TimeComplexity
    deq = deque([i for i in range(1, num + 1)])
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()

#     python 에서 queue를 사용할때, deque를 사용한다. append(), appendleft(), pop(), popleft() 기능이 있다.


#큐를 이용한 스택 구현
#235.Implement Stack using Queues
class MyStack():
    def __init__(self):
        self.queue = collections.deque()

    def push(self,value):
        self.queue.append(value)
        for _ in range(len(self.queue)-1) :
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
#selft.queue is None 으로 판별하면, collections.deque()로 만든 self.queue는 deque([])를 반환하기 때문에 안됨


#스택을 이용한 큐 구현
#232 Implement Queue using Stacks
class MyQueue :
    def __init__(self):
        self.stack = []

    def push(self,x):
        temp =[]
        for _ in range(len(self.stack)):
            temp.append(self.stack.pop())
        if len(self.stack) == 0 :
            self.stack.append(x)
        while len(temp) != 0 :
            self.stack.append(temp.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) ==0

queue = MyQueue();

queue.push(1)
queue.push(2)
print(queue.peek())
queue.pop()
print(queue.empty())

#원형 큐 디자인
#622.Design Circular Queue
class MyCircularQueue :
    def __init__(self,size):
        self.q = [None]* size
        self.front = 0
        self.rear = 0
        self.size = size
    def enQueue(self,x):

        #처음 상태 None 이라는거 자체가 비어있다는 소리지만 ponter가 같은곳을 가르키고 있는지도 한번더 확인해봄
        if self.rear == self.front and self.q[self.rear] is None:
            self.q[self.rear] = x
            return True
        #rear를 뒤로 한칸 이동한게 front 이면 꽉차있다는 소리이므로 enQueue 할 수 없다.
        #다음거가 None이든 아니든 크게 중요하지 않지만, dequeue에서 None을 넣어줄거임으로 한번더 확인하자
        if (self.rear +1) % self.size != self.front and self.q[(self.rear+1)%self.size] is None:
            #비어있을때 rear를 안이동하고 그냥 넣어준다
            self.rear = (self.rear +1) % self.size
            self.q[self.rear] = x
            return True
        #꽉 차있을 때
        else :
            return False

    def deQueue(self):
        #아무것도 안들어가 있을때
        if self.front == self.rear and self.front is None:
            return False

        #하나만 들어가있을때 -> 포인터 변경은 없다
        elif self.front == self.rear and self.front is not None:
            self.q[self.front] = None
            return True
        # 두포인터가 다를때 -> front 를 뒤로 한칸 이동
        else:
            self.q[self.front ] = None
            self.front = (self.front +1) % self.size
            return True

    def Rear(self):
        #비어있으면 -1 반환
        if self.q[self.rear] is None:
            return -1
        else:
            return self.q[self.rear]
    def Front(self):
        #비어있으면 -1 반환
        if self.q[self.front] is None:
            return -1
        else:
            return self.q[self.front]

    def isFull(self):
        return (self.rear +1) % self.size == self.front

circularQueue = MyCircularQueue(5);
circularQueue.enQueue(10)
circularQueue.enQueue(20)
circularQueue.enQueue(30)
circularQueue.enQueue(40)
circularQueue.Rear()
circularQueue.isFull()
circularQueue.deQueue()
circularQueue.deQueue()
circularQueue.enQueue(50)
circularQueue.enQueue(60)
circularQueue.Rear()
circularQueue.Front()

#백준 문제 1966
#중요도 Queue문제
def priorityQueue():
    test_case_number = int(input()) #text case의 수를 입력받는다

    #test_case의 수만큼 수행한다
    for _ in range(test_case_number):
        num, q = [int(x) for x in input().split(' ')] #문서의 갯수, 궁금한 문서
        priority = [int(p) for p in input().split(' ')] #중요도 인풋값
        s_prio = sorted(priority) #제일큰 priority 알고싶으니까 정렬해준거
        priority = collections.deque(priority)  # 중요도 인풋값을 큐로 만들어준다
        queue = collections.deque() #타겟 인덱스를 정장할 큐도 함께 만들어 준다
        c = 0
        for j in range(num):
            if j == q :
                queue.append("target")
            else:
                queue.append("-")
            t = "-"

        while t == "-":
            if priority[0] != s_prio[-1]:
                queue.append(queue.popleft())
                priority.append(priority.popleft())
            if priority[0] == s_prio[-1]:
                t = queue.popleft()
                priority.popleft()
                s_prio.pop()
                c +=1

                if t == "target":
                    print(c)


# priorityQueue()

#1
#38 29
#7 1 8 4 7 1 3 4 6 5 7 8 3 2 8 5 9 4 6 8 2 1 8 7 4 8 5 3 7 6 3 4 6 1 5 2 8 5

