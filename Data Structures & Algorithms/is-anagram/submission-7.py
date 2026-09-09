from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 'harsh' ==> {'h': 2, 'a': 1, 'r': 1, 's': 1}

        # s_counter = defaultdict()
        # t_counter = defaultdict()

        # for i in s:
        #     s_counter[i] = s_counter.get(i, 0) + 1
        # for i in t:
        #     t_counter[i] = t_counter.get(i, 0) + 1

        # return s_counter == t_counter
        return Counter(s) == Counter(t)

        

        