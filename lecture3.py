# Outline of an algorithm
"""
What are algorithms
- particular step to follow to solve a particular problem

characteristics of algorithm
- should be independent of any language
- It should be definite

criteria of algorithm
- finite input
- finite output
- finiteness
- definiteness

Steps to design an algorithm
- Device an algo -> find the best step
- Validation
- analysis
- Analysis of algo - TC, SC

Time Complexity
- No. of computations required to solve a problem
- TC = {Sum of frequency count of each instruction of algorithm}

Space Complexity
- Estimation of memory space required
- Space required by variable
- Space required by DS used
- Space required by Stack used in recursion algorithms
"""


# Algorithm Example - Palindrome check


def isPalindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            break
    return i == n // 2 - 1


print(isPalindrome("racecar"))
