class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # {value: index_of_this_value}
        # nums[i] + nums[j] == target
        # nums[j] = target - nums[i]

        for i in range(len(nums)):
            if target - nums[i] in seen.keys():
                return [seen[target-nums[i]],i]
            else:
                seen[nums[i]] = i
        


        