def solution(nums):
    nums_s = list(set(nums))
    k = len(nums) // 2
    return min(len(nums_s), k)