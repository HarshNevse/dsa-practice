class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        len_nums=len(nums)
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0) + 1

        buckets = [[] for i in range(len_nums + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        results = []

        for i in range(len_nums, -1, -1):

            if len(buckets[i]) > 0:
                results.extend(buckets[i][:k-len(results)])
                if len(results) == k:
                    return results
        return results
