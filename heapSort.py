import sys
import heapq

class BinaryMinHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

class BinaryMaxHeap():
    def __init__(self):
        self.items =[None]
    def __len__(self):
        return len(self) -1
    def _percolate_down(self,cur):
        left = cur * 2
        right = cur *2 +1
        biggest = cur

        if left < len(self) and self.items[left] > self.items[biggest]:
            biggest = left
        if right < len(self) and self.items[right] > self.items[biggest]:
            biggest = right
        if biggest != cur:
            self.items[ biggest], self.items[cur] = self.items [cur],self.items[biggest]
            self._percolate_down(biggest)
    def _percolate_up(self):
        cur = len(self)
        parent = cur// 2

        while parent >=1:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur//2
    def insert(self,val):
        self.items.append(val)
        self._percolate_up()
    def extract(self):
        if len(self) < 1 :
            return None

        root = self.items[1]

        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root
def sorted_by_heap(lst):
    maxheap = BinaryMaxHeap()
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))


def cardSort():
    read = sys.stdin.readline
    n = int(read())
    heap =[]
    answer = 0
    for _ in range(n):
        heapq.heappush(heap,int(read()))

    while len(heap) >1 :
        i = heapq.heappop(heap)
        j = heapq.heappop(heap)
        answer += (i+j)
        heapq.heappush(heap,i+j)

    print(answer)

cardSort()