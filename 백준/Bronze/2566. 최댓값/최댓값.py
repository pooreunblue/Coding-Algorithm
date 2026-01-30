arr = [list(map(int, input().split())) for _ in range(9)]
max_val = max(map(max, arr))
indices=[(i,j) for i in range(9) for j in range(9) if arr[i][j]==max_val]
print(max_val)
print(indices[0][0]+1, indices[0][1]+1)