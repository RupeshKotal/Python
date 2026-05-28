nums = [23, 11, 45, 78, 96, 54, 82]

total = 0
div = len(nums)

for num in nums:
    total = total + num

avg = total // div

print(avg)
