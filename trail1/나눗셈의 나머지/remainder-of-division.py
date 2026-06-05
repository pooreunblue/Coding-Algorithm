number = input().split()
a = 0
A, B = int(number[0]), int(number[1])
mod = [0] * B
while A > 1:
    mod[A%B] += 1
    A = A // B
for i in range(len(mod)):
    a += mod[i] ** 2
print(a)