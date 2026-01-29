s = input().upper()
dic = {}
for i in s:
    dic[i] = dic.get(i, 0) + 1
m = [k for k, v in dic.items() if v == max(dic.values())]
if len(m) > 1:
    print('?')
else: print(m[0])