class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        ans = 0
        for num in counts:
            if k > 0 and num + k in counts:
                ans +=1
            elif k == 0 and counts[num] > 1:
                ans += 1
        return ans
