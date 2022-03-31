# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head) :
    if not head :
        return
    key = head.next
    output = ListNode(head.val, None)
    header = output

    while key:
        # key 가 존재 하는 동안
        # key 값이 정렬된 마지막 인덱스 값보다 크다면 그냥 뒤에 붙인다
        if output.val <= key.val:
            output.next = ListNode(key.val, None)
            output = output.next
        #값이 작으면 맨 앞에 붙여준다
        if header.val > key.val:
            l = ListNode(key.val,header)
            header = l
        # key값이 작으면 값을 바꿔 준다
        else:
            insertNode(header, key.val)
        key = key.next


    return header

def insertNode(head, key):
    if not head :
        return
    header = head
    node = head.next
    prev = head
    if not node:
        if prev.val<key:
            prev.next = ListNode(key,None)
            return header

        else:
            l = ListNode(key,prev)

            return l
    while node:
        if prev.val >key:
            l = ListNode(key,prev)
            return l
        if prev.val <= key and key <= node.val:
            prev.next = ListNode(key, node)
            return header
        prev = node
        node = node.next

    node.next = ListNode(key, node)
    return header


l = ListNode(4)
q = ListNode(1)
q.next = ListNode(3)
l.next = ListNode(2,q)

insertionSortList(l)


def largestNumber(nums):
    # bubble sort
    if len(nums) == 0:
        return ""
    if len(nums) == 1:
        return str(nums[0])

    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if int(str(nums[j]) + str(nums[j + 1])) < int(str(nums[j + 1]) + str(nums[j])):

                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return ''.join(str(x) for x in nums)


# print(largestNumber([10,2]))

def numberBooks():
    testcase = int(input())

    for _ in range(testcase):
        n = int(input())
        arr = []
        state = True
        for _ in range(n):
            arr.append(input())
        arr.sort()

        for i in range(n-1):
            if arr[i+1][:len(arr[i])] == arr[i]:
                state =False
                break
        if state:
            print("YES")
        else:
            print("NO")

numberBooks()

