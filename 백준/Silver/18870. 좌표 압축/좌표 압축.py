import sys
import bisect 

n = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))
sorted_points = sorted(set(points))
for i in points:
    print(bisect.bisect_left(sorted_points, i), end = ' ')