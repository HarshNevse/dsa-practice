class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        len_nums=len(nums)
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        r = [[] for i in range(len_nums+1)]
        for number, frequency in counter.items():
            r[frequency].append(number)
        result = []
        for i in range(len_nums, -1,-1):
            if len(r[i]) > 0:
                result.extend(r[i][:k-len(result)])
                if len(result) == k:
                    return result