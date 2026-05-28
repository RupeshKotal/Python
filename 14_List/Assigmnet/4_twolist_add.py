nums1 = [23, -11, 45, 78, -96, 54, 82]
nums2 = [43, 56, 7, 34, 56, 78, 5, 67]


def listadd(nums1, nums2):
    new_list = []
    n = len(nums1) - 1

    for i in range(0, n):
        total = nums1[i] + nums2[i]
        new_list.append(total)

    return new_list


ans = listadd(nums1, nums2)
print(ans)
