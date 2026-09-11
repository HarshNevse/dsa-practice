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
        r = []
        for number, frequency in list(counter.items()):
            r.append([frequency,number])
        r.sort(reverse=True)

        final_result_list = []
        for i in range(k):
            final_result_list.append(r[i][1])

        return final_result_list