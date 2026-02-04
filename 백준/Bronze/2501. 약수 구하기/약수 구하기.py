n, k = map(int, input().split())
divisors = set()
for i in range(1, n//2):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n//i)
a = sorted(divisors)
if len(a) < k:
    print(0)
else: 
    print(a[k-1])