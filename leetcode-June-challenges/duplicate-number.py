def findDuplicate(nums) -> int:
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            return nums[i]


if __name__ == '__main__':
    print(findDuplicate([1, 3, 4, 2, 2]))
