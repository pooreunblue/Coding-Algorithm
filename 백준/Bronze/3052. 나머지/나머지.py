d = []
for _ in range(10):
    d.append((int(input()) % 42))
print(len(set(d)))