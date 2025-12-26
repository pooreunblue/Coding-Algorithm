def solution(numbers):
    num1 = max(numbers)
    numbers.remove(num1)
    return num1 * max(numbers)