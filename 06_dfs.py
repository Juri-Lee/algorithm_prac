#DFS 구현
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def dfs_recursive(node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited


def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited
print(dfs_stack(1))
#예제 섬의 개수
#STACK :
def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

#RECURSIVE:
def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

#DFS 테스트 코드

assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]

def letterCombinations(digits):
    result =[]
    numToText = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyx"
    }
    def dfs(index,path):
        if len(digits) == len(path):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in numToText[digits[i]]:
                dfs(i+1, path +j)

    if not digits:
        return []
    dfs(0,"")

    return result

print(letterCombinations("23"))

def Permutations(list):
    result =[]

    def dfs(elem):
        print(type(elem))
        if len(elem) == len(list):
            result.append(elem)

        for j in range(len(elem),len(list)):
            for i in list:
                if i not in elem:
                    elem.append(i)
                    dfs(elem)

    for elem in list:
        temp =[]
        temp.append(elem)

        dfs(temp)
    return result

print(Permutations([1,2,3]))


def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            # s(시작점)가 아닌 i(뻗어나가는 가지)에 +1
            DFS(L + 1, i + 1)


# n, m = map(int, input().split())
# res = [0] * (n + 1)
# cnt = 0
# DFS(0, 1)
# print(cnt)

def numbering_complex(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt

def combine(n,k):
    results = []

    def dfs(elements, start):
        if len(elements) == k :
            results.append(elements[:])
            return

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements,i+1)
            elements.pop()
    dfs([],1)
    return results

print( combine(4,2))

def permutataionk(nums):
    result = []
    prev_elem = []
    def dfs(elem):
        if len(elem) == 0:
            result.append(prev_elem[:])

        for i in elem:
            next_elem = elem[:]
            next_elem.remove(i)

            prev_elem.append(i)
            dfs(next_elem)
            prev_elem.pop()

    dfs(nums)
    return result

print("permutation :" , permutataionk([1,2,3]))


def combinations(n,k):
    result=[]
    def dfs(elems,start,k):
        if k ==0 :
            result.append(elems[:])
            return
        for i in range(start, n+1):
            elems.append(i)
            dfs(elems,i+1, k-1)
            elems.pop()

    dfs([],1,k)
    return result

print("combinations: ",combinations(4,2))

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])

    cnt = 0
    #섬
    stack = []
    #섬의 좌표
    for row in range(rows):
        for col in range(cols):
            #좌표생성
            if grid[row][col] != '1':
                # 방문한곳이 1인지 아닌지 본다
                continue
            # 아니면 그냥지나감
            cnt += 1
            stack.append((row, col))
            # 1이라면 섬숫자 올리고 좌표 스택으로
            while stack:
                tmp = stack.pop()
                #좌표 스택으로 뺌
                y, x = tmp #
                # 방문한 좌표 스택에서 빼서 표시
                grid[y][x] = '0'
                # 방문한 1은 0으로 변환
                # 1. 북으로 갈 수 있는가?
                if y > 0:
                    # 북쪽 탐색 후 섬이면 스택에 저장
                    if grid[y - 1][x] == '1':
                        stack.append((y - 1, x))
                # 2. 서로 갈 수 있는가?
                if x > 0:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y][x - 1] == '1':
                        stack.append((y, x - 1))
                # 3. 남으로 갈 수 있는가?
                if y < rows - 1:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y + 1][x] == '1':
                        stack.append((y + 1, x))
                # 4. 동으로 갈 수 있는가?
                if x < cols - 1:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y][x + 1] == '1':
                        stack.append((y, x + 1))
            return cnt
        # 단, stack은 역순으로 출력(pop)이 이루어지므로 실질적인 탐색순서는 동 -> 남 -> 서 -> 북이 됨



numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])
