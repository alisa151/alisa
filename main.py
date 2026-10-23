def square_positives(nums):
    return [x**2 for x in nums if x > 0]
numbers = [-5, 3, 0, -1, 4, 2]
print(square_positives(numbers))
