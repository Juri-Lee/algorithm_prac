def factorial(n):
    if n ==1 or n==0 :
        return 1
    return n* factorial(n-1)

# print(factorial(int(input())))

def fibonach(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n >=2:
        return fibonach(n-1) + fibonach(n-2)

# print(fibonach(int(input)))

def stars(n):
    if n ==1:
        return "*"

    num= int(n/3)
    return stars(num)*n+"\n"+stars(num)+num*" "+stars(num)+"\n"+n*stars(num)

print(stars(9))

# def virus():
#     n = int(input())
#     def dfs():



