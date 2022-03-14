import collections
import string


def get_idx(word):
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        indx = ord(char) - 97

        if result[indx] == -1:
            result[indx] = i

    print(' '.join([str(num) for num in result]))


def group_anagram(arr):
    ann = collections.defaultdict(list)

    for word in arr:
        key = ''.join(sorted(word))
        ann[key].append(word)
    print(list(list(ann.values())))


def longest_palindrome(str):
    longest = ''
    for i in range(len(str)):
        sub = str[i]
        b = i - 1
        f = i + 1
        while b >= 0 and f < len(str):
            if str[b] == str[f]:
                sub = str[b] + sub + str[f]
                b = b - 1
                f = f + 1
            else:
                break
        if len(longest) < len(sub):
            longest = sub

    return longest


longest_palindrome("babad")


def longest_palindrome_2(str):
    scaleodd = 3
    scaleeven = 2

    def check(str, len):
        i = 0
        k = len - 1
        while (i < k):
            if str[i] is str[k]:
                i = i + 1
                k = k - 1
            else:
                return False

            return True

    for i in range(len(str)):
        if check(str[i:i + scaleeven], scaleeven):
            resulteven = str[i:i + scaleeven]
            scaleeven += 2

        if check(str[i:i + scaleodd], scaleodd):
            resultodd = str[i + scaleodd]
            scaleodd += 2

    result = max(resulteven, resultodd)
    return result


def longestPalindrome(s):
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range((len(s) - 1)):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


longestPalindrome("babad")


def three_sum(arr):
    arr.sort()
    result = []
    A = [x for x in arr if x == 0]
    B = [x for x in arr if x > 0]
    C = [x for x in arr if x < 0]
    A.sort()
    B.sort()
    C.sort()
    print(A)
    for i in range(len(B)):
        if i < len(B) - 1 and B[i + 1] == B[i]:
            continue
        else:
            for j in range(len(C)):
                if j < len(C) - 1 and C[j + 1] == C[j]:
                    continue
                else:
                    if (B[i] + C[j] == 0) and A:
                        result.append([B[i], C[j], 0])

                    elif (B[i] + C[j] == 0) and A == -1:
                        continue
                    else:
                        if B[i] + C[j] > 0:
                            for k in range(len(C)):
                                if j is not k and B[i] + C[j] + C[k] == 0:
                                    result.append([B[i], C[j], C[k]])
                                else:
                                    continue
                        if B[i] + C[j] < 0:
                            for k in range(len(B)):
                                if k is not i and B[i] + C[j] + B[k] == 0:
                                    result.append([B[i], C[j], B[k]])
                                else:
                                    continue

    return result


print(three_sum([1, -1]))


def three_sum_itor(arr):
    arr.sort()
    i = 0;
    result = []
    k = len(arr) - 1

    for j in range(1, len(arr) - 1):
        while (i < k):
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                i = i + 1
                if i == j:
                    i = j

                while arr[i] == arr[i + 1]:
                    i = i + 1
            elif sum > 0:
                k = k - 1
                if (k == j):
                    k = j

                while (arr[k] == arr[k - 1]):
                    k = k - 1
            elif sum == 0:
                result.append([arr[i], arr[j], arr[k]])

                break

        return result


# sort해서 앞이랑 뒤부터 i, k 주고 j 만 이동시키는게 낫겟다


# def array_partition(arr):
#     arr.sort()
#     sum = 0
#     for i in range(len(arr)):
#         if i%2 == 0 :
#             sum += arr[i]
#
#     return sum

def longestPalindrome(str):
    def isPalindromme(start, end):
        s = start
        e = end
        while s <= e:
            if str[s] == str[e]:
                s = s + 1
                e = e - 1
                continue
            else:
                return False
        return True

    s_even = 0
    even_scale = 1
    result_even= ''
    while s_even + even_scale < len(str) :
        if (isPalindromme(s_even, s_even + even_scale)):
            result_even = str[s_even:s_even + even_scale + 1]
            even_scale = even_scale+ 2
            s_even = s_even-1
            if s_even <0 :
                s_even = 0
            print(s_even, result_even,even_scale)
        else:
            s_even += 1

    s_odd = 0
    odd_scale = 2
    result_odd =''
    while s_odd + odd_scale < len(str) :
        if (isPalindromme(s_odd, s_odd + odd_scale)):
            result_odd = str[s_odd:s_odd + odd_scale + 1]
            odd_scale = odd_scale+ 2
            s_odd = s_odd -1
            if s_odd < 0
                s_odd =0
        else:
            s_odd += 1
    return max(result_odd, result_even, key=len)


class Solution:
    def longestPalindrome(self, p):

        def isPalindromme(start, end):
            s = start
            e = end
            while s <= e:
                if p[s] == p[e]:
                    s = s + 1
                    e = e - 1
                    continue
                else:
                    return False
            return True

        s_even = 0
        even_scale = 1
        result_even = ''
        while s_even + even_scale < len(p):
            if (isPalindromme(s_even, s_even + even_scale)):
                result_even = p[s_even:s_even + even_scale + 1]
                even_scale = even_scale + 2
                s_even = s_even - 1
                if s_even < 0:
                    s_even = 0
                print(s_even, result_even, even_scale)
            else:
                s_even += 1

        s_odd = 0
        odd_scale = 0
        result_odd = ''
        while s_odd + odd_scale < len(p):
            if (isPalindromme(s_odd, s_odd + odd_scale)):
                result_odd = p[s_odd:s_odd + odd_scale + 1]
                odd_scale = odd_scale + 2
                s_odd = s_odd - 1
                if s_odd < 0:
                    s_odd = 0
            else:
                s_odd += 1
        return max(result_odd, result_even, key=len)

# Runtime: 1329 ms, faster than 57.56% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.1 MB, less than 43.52% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s):
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result

# Runtime: 388 ms, faster than 92.43% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 75.41% of Python3 online submissions for Longest Palindromic Substring.
