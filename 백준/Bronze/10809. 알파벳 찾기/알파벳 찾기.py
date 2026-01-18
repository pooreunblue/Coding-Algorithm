s = input()
a = []
for i in range(97, 123):
    c = chr(i)
    a.append(str(s.find(c)))
print(' '.join(a))