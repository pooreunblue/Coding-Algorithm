n = int(input())
a = []
for i in range(1, n):
    da = [(int(d)) for d in str(i)]
    if i+sum(da) == n:
        a.append(i)
if len(a) > 0:
    print(a[0])
else:
    print(0)
    