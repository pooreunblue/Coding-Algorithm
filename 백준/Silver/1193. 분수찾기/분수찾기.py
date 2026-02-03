x = int(input())
n = 1
while x > n:
    x -= n
    n += 1
if n % 2 == 0:
    a = x
    b = n+1-x
else :
    a = n+1-x
    b = x
print(f'{a}/{b}')