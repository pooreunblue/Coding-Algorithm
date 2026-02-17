import sys

N = int(sys.stdin.readline())
member = []
for i in range(1, N+1):
    data = sys.stdin.readline().split()
    member.append([i, int(data[0]), data[1]])
member = sorted(member, key = lambda x: (x[1], x[0]))
for m in member:
    print(m[1], m[2])