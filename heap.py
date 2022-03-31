import sys
import heapq

class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]
    def __len__(self):
        return len(self.items) -1
    def _percolate_up(self):
        cur = len(self)
        parent = cur //2

        while parent > 1:
            if self.items[cur] > self.items[parent]:
                self.items[cur] ,self.items[parent]  = self.items[parent], self.items[cur]
                cur = parent
                parent = cur//2

    def _percolate_down(self,cur):
        biggest  = cur
        left = cur *2
        right = cur *2 +1

        if left < len(self) and self.items[biggest] < self.items[left]:
            biggest = left
        if right <len(self) and self.items[biggest] < self.items[right]:
            biggest = right
        if biggest != cur :
            self.items[cur], self.items[biggest ] =  self.items[biggest], self.items[cur]
            self._percolate_down(biggest)
    def insert(self,k):
        self.items.append(k)
        self._percolate_up()
    def extract(self):
        if len(self) <1 :
            return None

        root = self.lists[1]
        self.lists[1] = self.list[-1]
        self.lists.pop()
        self._percolate_down(1)

        return root

def test_maxheap_we_made(lst,k):
    maxheap = BinaryMaxHeap()
    for elem in lst:
        maxheap.insert(elem)
    for _ in range(k-1):
        maxheap.extreact()

    return maxheap.extract()

#최소 힙
class Minheap:
    def __init__(self):
         self.items = [None]

    def __len__(self):
        return len(self.items) -1

    def _percolate_up(self):
        cur = len(self)
        parent = cur //2
        while parent >=1:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur //2

    def _percolate_down(self,i):

        smallest = i
        right = i*2+1
        left = i*2

        if right < len(self ) and self.lists[right] < self.lists[smallest]:
            smallest =right
        if left < len(self) and self.lists[left] < self.lists[smallest]:
            smallest = left
        if smallest != i:
            self.list[i], self.lists[smallest] = self.lists[smallest], self.lists[i]
            self._percolate_down(smallest)
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1 :
            return 0
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

def MinheapProb():
    read = sys.stdin.readline
    minheap = Minheap()
    n = int(read())
    result = []
    for _ in range(n):
        k = int(read())
        if k != 0 :
            minheap.insert(k)
        else :
            result.append(minheap.extract())
    print('\n'.join([str(x) for x in result]))

# MinheapProb()

def Minheap_with_heapq():
    read = sys.stdin.readline
    h = []
    result = []
    n = int(read())
    for _ in range(n):
        k = int(read())
        if len(h) == 0  and k ==0:
            result.append(0)
        elif k == 0 :
            result.append(heapq.heappop(h))
        else:
            heapq.heappush(h,k)

    print('\n'.join([str(x) for x in result]))



def Maxheap_with_heapq():
    read = sys.stdin.readline
    h = []
    result = []
    n = int(read())
    for _ in range(n):
        k = int(read())
        if len(h) == 0 and k ==0:
            result.append(0)
        elif k == 0 :
            result.append(-heapq.heappop(h))



        else:
            heapq.heappush(h,-k)

    print('\n'.join([str(x) for x in result]))

Maxheap_with_heapq()