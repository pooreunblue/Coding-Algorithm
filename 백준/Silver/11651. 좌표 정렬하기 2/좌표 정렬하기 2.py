import sys

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append([y, x])
points = sorted(points)
for point in points:
    print(point[1], point[0])
