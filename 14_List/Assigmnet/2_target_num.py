nums = [23, -11, 45, 78, -96, 54, 82]


target = int(input("Enter target num : "))


def does_exist(target, nums):
    for num in nums:
        if target == num:
            return True
        
    return False



ans = does_exist(target, nums)
print(ans)
