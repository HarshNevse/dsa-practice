class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [0,1,2]
        l_nums=list(set(nums))
        if len(l_nums) == k:
            return l_nums
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        # print(f"Counter: {counter.items()}")
        r = [[] for i in range(len(nums)+1)]
        # print(r)
        for number, frequency in list(counter.items()):
            #print(f"r[{frequency}].append({number})")
            r[frequency].append(number)
        # print(r)
        result = []
        for i in range(len(nums), -1,-1):
            if len(r[i]) > 0:
                result.extend(r[i][:k])
                # print(result)
                if len(result) == k:
                    return result