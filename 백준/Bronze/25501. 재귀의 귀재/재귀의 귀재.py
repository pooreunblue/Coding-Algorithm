import sys

T = int(input())

def recursion(S, l, r):
    global cnt
    cnt += 1
    if l>=r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S, l+1, r-1)
    
def isPalindrome(S):
    global cnt
    cnt = 0
    return recursion(S, 0, len(S)-1)
    
for i in range(T):
    S = input().strip()
    print(isPalindrome(S), cnt)