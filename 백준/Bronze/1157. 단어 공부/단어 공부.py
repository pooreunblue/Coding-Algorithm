s = list(input().upper())
dic = {}
for i in set(s):
    dic[i] = s.count(i)
for key, value in dic.items():
    m = [k for k, v in dic.items() if v == max(dic.values())]
if len(m) ==  1:
    print(*m)
else: print('?')