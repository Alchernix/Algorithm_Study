N, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers)
print(numbers[K - 1])
