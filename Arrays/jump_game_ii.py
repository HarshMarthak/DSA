class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        ans = 0
        while r < len(nums) - 1:
            ans += 1
            maxx = max([i + nums[i] for i in range(l,r+1)])
            l,r = r+1, maxx
        return ans
