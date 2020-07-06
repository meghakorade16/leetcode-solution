def searchInsert(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums)


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 7))
