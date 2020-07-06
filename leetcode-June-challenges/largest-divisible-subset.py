def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    sol = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(sol[i]) < (len(sol[j]) + 1):
                sol[i] = sol[j] + [nums[i]]
                print(sol)
    return max(sol, key=len)


if __name__ == '__main__':
    print(largestDivisibleSubset([1, 2, 4, 8]))