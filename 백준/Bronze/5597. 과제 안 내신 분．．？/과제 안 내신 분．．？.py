numbers = []
a = []
while True:
    try:
        numbers.append((int(input())))
    except:
        break

for i in range(1, 31):
    if i not in numbers:
        a.append(i)
        
print(min(a))
print(max(a))