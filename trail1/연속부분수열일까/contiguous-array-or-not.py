A, B = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
idx = []
result = 'No'
for i in range(A):
    if list_B[0] == list_A[i]:
        idx.append(i)
for i in idx:
    for j in range(B):
        if i+j < A and list_A[i+j] == list_B[j]:
            result = 'Yes'
        else:
            result = 'No'
    if result == 'Yes':
        break
print(result)