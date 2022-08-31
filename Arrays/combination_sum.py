class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(left, path, idx):
            if not left:
                res.append(path[:])
            else:
                for i, val in enumerate(candidates[idx:]):
                    if val > left:
                        break
                    dfs(left - val, path + [val], idx + i)
        dfs(target, [], 0)
        return res
