from _ast import List


class Solution:
    def deccompressRLElist(nums):
        output = []
        # length = len(nums)-1 if len(nums)<=2 else len(nums)/2
        for i in range(0, int(len(nums)/2)):
            output.extend([nums[i*2+1]] * nums[i*2])
        print(output)

    deccompressRLElist([1, 2, 3, 4])

# class Solution:
#     def decompressRLElist(nums):
#         output = []
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 for j in range(nums[i]):
#                     output.append(nums[i + 1])
#         print(output)
#     decompressRLElist([1, 2, 3, 4])
