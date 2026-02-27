import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
stk = []
i = 1
while numbers:
  if numbers[0] == i:
    numbers.pop(0)
    i += 1
  elif len(stk) > 0 and stk[-1] == i:
    stk.pop()
    i += 1
  else:
    stk.append(numbers[0])
    numbers.pop(0)
while stk:
  if stk[-1] == i:
    stk.pop()
    i += 1
  else:
    print('Sad')
    break
if len(stk) == 0:
  print('Nice')