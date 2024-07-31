# Given two strings s and t return true if t is an anagram of s and false otheriwise.
# anagram is a word or phrase formed by rearranging the ltter of a different word or phrase.  Using all the letters exactly once.


def isAnagram(s: str, t: str) -> bool:
    s_list: list = list(s)
    s_list.sort()
    t_list: list = list(t)
    t_list.sort()
    if s_list == t_list:
        return True
    return False

print(isAnagram(s="rat", t="cat"), "false")