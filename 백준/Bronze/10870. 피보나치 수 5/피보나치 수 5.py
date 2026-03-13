import sys

n = int(sys.stdin.readline())
a = []
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    f = fibonacci(n-1) + fibonacci(n-2)
    return f
for i in range(n+1):
  a.append(fibonacci(i))
print(a[n])