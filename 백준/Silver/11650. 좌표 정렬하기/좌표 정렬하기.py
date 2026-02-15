import sys

n = int(sys.stdin.readline())
points = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  points.append([x, y])
points = sorted(points)
for point in points:
    print(*point)