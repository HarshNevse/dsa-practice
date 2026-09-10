class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {} # {(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) : ['ate','tea','eat']}

        for i in strs:
            temp_list = [0]*26
            for char in i:
                temp_list[ord(char)-97] += 1
            tup = tuple(temp_list)
            anagram_map[tup] = anagram_map.get(tup,[])
            anagram_map[tup].append(i)

        return list(anagram_map.values())
            

        