import collections
from collections import deque, defaultdict

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]

def island_bfs(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            q = deque([(row, col)])

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    grid[nx][ny] = '0'
                    q.append((nx, ny))
    return cnt


assert island_bfs(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_bfs(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

#39.Combination Sum
def combinationSum(candidates, target):
    q = deque(candidates)
    visited = deque([[]])
    answer = []
    temp = []
    while q and visited :
        search = q.popleft()
        visit = visited.popleft()
        for i in candidates:
            q.append(i)

        for i in range(len(candidates)):
            for i in candidates:
                q.append(i)
            if search + sum(visit) <= target and len(visit) <= len(candidates):
                visit.append(search)
                if sum(visit) == target and sorted(visit) not in answer:
                    answer.append(sorted(visit[:]))
                else:
                    visited.append(visit[:])
                visit.pop()
            search = q.popleft()
    print(answer)


combinationSum([2,3,5],8)

#78.subsets DFS
def subsets(nums):
    answer = []
    def dfs(index, subsets):

        answer.append(subsets)
        for i in range(index,len(nums)):
            dfs(i+1,subsets +[nums[i]])
    dfs(0,[])

    return answer


print(subsets([1,2,3]))

def Reconstruct_flight(sch):
    #연결리스트 그래프 만들기
    schedule =collections.defaultdict(list)
    for flight in sch:
        schedule[flight[0]].append(flight[1])
    print(schedule)
    root = "JFK"
    result =[]
    def dfs(start):
        com = [start]
        q = deque()
        q.append(schedule[start])
        if not schedule[start]:
            return result

        for fli in schedule[start]:
            com.append(fli)
            if com[0] == "JFK":
                result.append("JFK")
            result.append(fli)
            dfs(fli)
            com.pop()

    dfs(root)
    print(result)

def Reconstruct_flight_k(sch):
    #연결리스트 그래프 만들기
    inlist = sch
    a=1
    while a>0:
        for i in inlist:
            depart = i[0]
            arrv = i[-1]

            for j in inlist:
                if arrv == j[0]:
                    i.append(j[-1])
                if depart ==j[-1]:
                   j =  j + i[1:]
        a-=1


    print(inlist)



Reconstruct_flight_k([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
