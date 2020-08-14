def threeSum(nums):
    length = len(nums)
    if length < 3:
        return []
    nums.sort()
    result = set()
    for i in range(0, length - 2):
        j, k = i + 1, length - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                result.add(tuple([nums[i], nums[j], nums[k]]))
                j += 1
                k -= 1
    return [list(element) for element in result]


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
