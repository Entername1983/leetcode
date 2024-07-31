
## store max length

## 2 pointers, left and right
## have hashmap with letter as key and index as value
## traverse through string, if we find a value in the hashmap, reset start to value after the one we have removed, _+ remove value






def lengthOfLoingestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    st: int = 0
    max_v: int = 0
    i = 1
    while i < len(s):
        print(f"i, {i}, st, {st}, range, {s[st:i]} value {s[i]}")
        while s[i] in s[st:i]:
            print("value in substring, incrementing start")
            st += 1
        i += 1
        max_v = max(max_v, len(s[st:i]))

    return max_v
        
        



print(lengthOfLoingestSubstring("au"))
print(lengthOfLoingestSubstring("abcabcbb"))