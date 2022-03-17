def numbers(*nums):

    total = 0
    for num in nums:
        total += num
        return total

print(numbers(1,2,3,4,5))