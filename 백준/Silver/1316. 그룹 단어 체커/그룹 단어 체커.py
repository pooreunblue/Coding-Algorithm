n = int(input())
count = 0
for i in range(n):
    s = input()
    if list(s) == sorted(s, key = s.find):
        count += 1
print(count)
