class Solution:
    def __init__(self):
        self.arr = []
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        list_res = []
        nums.sort()
        for qu in queries:
            count = 0
            for nu in nums:
                if qu>=nu:
                    qu -= nu
                    count +=1
            list_res.append(count)
        return list_res
