def strStr(haystack: str, needle: str) -> int:
    
    ## loop through haystack looking for first letter of needle.  
    ## if found move to second letter 
    ## need to keep track of how many letters in needle we have gone through
    ## if we the count of letters we have gone through == length of needle then return current index in haystack - length of needle
    
    ## if needle is longer than haystack then it can't be a substring, return -1
    if len(needle) > len(haystack):
        return -1
    
    
    for i, value in enumerate(haystack): ## loop through every letter in the haystack
        n_i = 0 ## need to keep track of the index of the needle
        if value == needle[n_i]: ## if the first letter matches, check the rest
            j = i ## start a new loop starting out at the first letter that matches from previous loop
            for j in range(j, min(j + len(needle), len(haystack))):
                # print("_______________________")
                # print('letter haystack inner loop', j, haystack[j])
                # print('letter needle inner loop', n_i, needle[n_i])
                if haystack[j] != needle[n_i]: ## check if the letters match, if they don't break out of the inner loop
                    break
                # print("its a match")
                if n_i == len(needle) - 1:
                    print("WE FOUND A MATCH", i)
                    return i
                n_i += 1 ## its a match, increment the index 
                j += 1
    print("NO STRING MATCHIN")
    return -1

strStr("mississippi", "issipi")
strStr("mississippi", "issipp")
strStr("mississippi", "issipp")
strStr("sadbutsad", "sad")
strStr("leetcode", "leeto")



# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

#         if len(haystack) < len(needle):
#             return -1

#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)] == needle:
#                 return i

#         return -1 