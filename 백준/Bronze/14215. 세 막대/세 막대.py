a, b, c = map(int, input().split())
tri = [a, b, c]
if a == b == c:
    print(a+b+c)
else:
    if sum(tri) - max(tri) > max(tri):
        print(sum(tri))
    else:
        print((sum(tri)-max(tri))*2-1)