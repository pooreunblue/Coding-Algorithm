numbers = [0] * 10
N = int(input())
nums = list(map(int, input().split()))
for num in nums:
    numbers[num] += 1
for i in range(1,10):
    print(numbers[i])