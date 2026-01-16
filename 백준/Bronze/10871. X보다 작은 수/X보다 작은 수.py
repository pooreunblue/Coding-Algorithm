l, x = map(int, input().split())
numbers = input().split()
a = []
for n in numbers:
    if int(n) < x:
        a.append(n)  
print(' '.join(a))