class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            b1 = x >> i & 1
            b2 = y >> i & 1
            if b1 != b2:
                ans += 1
        return ans
