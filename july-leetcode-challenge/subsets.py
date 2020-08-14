from collections import deque


def findSubsets(nums, result, index):
    if index < 0:
        print(list(result))
        return
    result.append(nums[index])
    findSubsets(nums, result, index - 1)
    result.pop()
    while index > 0 and nums[index] == nums[index - 1]:
        index -= 1
    findSubsets(nums, result, index - 1)


def subsets(nums):
    result = deque()
    findSubsets(nums, result, len(nums) - 1)


if __name__ == '__main__':
    subsets([1, 2, 3])
