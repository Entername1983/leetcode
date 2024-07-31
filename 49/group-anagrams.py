##  Given an array of strings strs, group the anagrams together.  You can return the anser in any order
## 
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ## keep track of the index of each string
    
    ## sort each string, groupt them into a list and put them back.  
    mapping: defaultdict = defaultdict(list)
    final_list: list[list[str]] = []
    for i, value in enumerate(strs):
        sorted_v = "".join(sorted(value))
        mapping[str(sorted_v)].append(i)
    i: int = 0
    for key in mapping.items():
        sub_list: list = []
        for j in mapping[key[0]]:
            sub_list.append(strs[j])
        final_list.append(sub_list)
        i += 1
    return final_list
        
    
    


print(groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]), ' ##### ["bat"],["nat","tan"],["ate","eat","tea"]]')