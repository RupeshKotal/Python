nums = [23, 11, 45, 78, 96, 54, 82]


def sorted(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


ans = sorted(nums)
print(ans)
