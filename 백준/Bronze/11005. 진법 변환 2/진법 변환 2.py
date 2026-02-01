n, b = map(int, input().split())
a = ''
mods = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n != 0:
    n, mod = divmod(n, b)
    a += mods[mod]
print(a[::-1])