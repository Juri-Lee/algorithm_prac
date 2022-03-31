import sys
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


def stageclear(N, stages):
    answer = []
    leftstage = len(stages)
    for i in range(1, N + 1):

        if leftstage < 1:
            answer.append([i,0])
            continue

        count = stages.count(i)
        fail = count / leftstage
        leftstage -= count
        answer.append([i, fail])

    a = sorted(answer, key=lambda x: (x[1], -x[1]), reverse=True)
    answer = [re[0] for re in a]

    return answer

stageclear(8,[2])

def wordsSort():
    read = sys.stdin.readline
    n = int(read())
    words = set()
    for _ in range(n):
        w = read().strip()
        words.add(w)

    words = list(words)
    words.sort()
    words.sort(key=len)

    for word in words:
        print(word)
wordsSort()