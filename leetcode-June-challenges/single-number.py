def singleNumber(nums):
    return (sum(set(nums)) * 3 - sum(nums)) // 2
    # for i in nums:
    #     if nums.count(i) == 1:
    #         return i

    # def singleNumber(self, nums: List[int]) -> int:
    #     ones, twos, thrice = 0, 0, 0
    #     for n in nums:
    #         twos = twos | (ones & n)
    #         ones = ones ^ n
    #         thrice = ones & twos
    #         ones &= ~thrice
    #         twos &= ~thrice
    #
    #     return ones


if __name__ == '__main__':
    print(singleNumber([2, 2, 3, 2]))
