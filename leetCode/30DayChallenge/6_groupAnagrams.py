# Given an array of strings, group anagrams together.

"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for index, word in enumerate(strs):
            key = "".join(sorted(word))
            if words.get(key) is None:
                val = []
            else:
                val = words.get(key)
            words.update({key: val + [index]})
        answer = []
        
        for key in words.keys():
            group = list(map(lambda x: strs[x], words.get(key)))
            answer.append(group)
        return answer
            
