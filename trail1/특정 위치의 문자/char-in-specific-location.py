words = ['L','E','B','R','O','S']
char = input()
index = 'None'
for i in range(len(words)):
    if char == words[i]:
        index = i
print(index)