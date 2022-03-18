
import collections
import math

def k(progresses, speeds):
    answer = []
    prog = collections.deque()
    for i in range(len(progresses)):
        prog.append(math.ceil((100-progresses[i])/speeds[i]))
    if prog:
        cur = prog.popleft()
    else :
        return answer
    if prog:
        next = prog.popleft()
    else :
        answer.append(1)
        return answer
    while cur :
        count = 1
        while cur >= next:
            if prog :
                next = prog.popleft()
                count +=1
            else:
                count += 1
                answer.append(count)
                return answer
        answer.append(count)
        if prog:
            cur,next = next, prog.popleft()

        if cur < next:
            answer.append(1)
            if prog:
                cur, next = next, prog.popleft()
            else:
                return answer
    return answer

print(k([95,90,99,99,80,99],[1,1,1,1,1,1]))

import collections

def p(bridge_length, weight, truck_weights):

        answer = 0
        bridge = collections.deque([0] * bridge_length)
        trucks = collections.deque(truck_weights)
        bweight =0
        while len(bridge):
            answer += 1
            truck = bridge.popleft()
            bweight -= truck
            if trucks:
                if bweight + trucks[0] <= weight:
                    add =trucks.popleft()
                    bridge.append(add)
                    bweight+= add
                else:
                    bridge.append(0)

        return answer


print(p(2,10,[7,4,5,6]))