def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0


def solution2(files):
    separate=[]
    answer = []
    for file in files:
        i=0
        while i < len(file):
            if file[i].isalpha() or file[i] == " " or file[i]  == "." or file[i]=="-":
                i+=1
            else:
                break
        alphas = file[0:i]
        j= i
        while j <len(file):
            if file[j].isdigit():
                j+=1
            else:
                break

        nums = file[i:j]
        tail = file[j:]
        separate.append([alphas,nums,tail])
    separate.sort(key=lambda x:(x[0].lower(), int(x[1]) ))


    for elem in separate:
        answer.append("".join(elem))
    print(answer)
    return answer


solution2( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

