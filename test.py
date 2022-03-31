def solution(dirs):
    answer = 0
    x = 0
    y = 0
    visited = []
    for dir in dirs:
        if dir == "U" and y < 5:
            y += 1
        elif dir == "L" and x > -5:
            x -= 1
        elif dir == "R" and x < 5:
            x += 1
        elif dir == "D" and y > -5:
            y -= 1
        else:
            continue
        if [x,y] not in visited :
            visited.append([x,y])
        else:
            for i in range(len(visited)):
                if visited[i] ==[x,y] and i>=1 :
                    if visited[i-1] != visited[-1]:
                        visited.append([x,y])
    answer = len(visited)
    return answer

# print(solution("LULLLLLLU"))


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(i, cal):
        print("in")
        if i == n:
            if cal == target:
                print(cal, target)
                nonlocal answer
                answer += 1
            return

        dfs(i + 1, cal + numbers[i])
        dfs(i + 1, cal - numbers[i])

    dfs(0, 0)
    return answer

print(solution([1,1,1,1,1],3))