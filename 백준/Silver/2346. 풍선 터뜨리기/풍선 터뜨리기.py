from collections import deque
import sys

N = int(sys.stdin.readline())
balloon = deque([i for i in range(1, N+1)])
answer = []
turn = 0
numbers = deque(list(map(int, sys.stdin.readline().split())))
for _ in range(N):
    turn = numbers[0]
    if turn > 0:
      answer.append(balloon.popleft())
      numbers.popleft()
      balloon.rotate(-1*(turn)+1)
      numbers.rotate(-1*(turn)+1)
    else:
      answer.append(balloon.popleft())
      numbers.popleft()
      balloon.rotate(-1*(turn))
      numbers.rotate(-1*(turn))
print(*answer)