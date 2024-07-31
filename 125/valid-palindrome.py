def isPalindrome(s: str) -> bool:

    r: int = len(s) - 1
    l: int = 0
    for _ in range(len(s)):
        print(s[l], s[r])
        if s[r].isalnum() and s[l].isalnum():
            print(s[l], s[r])
            if s[r].lower() != s[l].lower():
                return False
            r -=1
            l +=1
        else:
            if not s[r].isalnum():
                r -= 1
            if not s[l].isalnum():
                l += 1
    return True


# print(isPalindrome(s = "A man, a plan, a canal: Panama"))
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        return s==s[::-1]
print(isPalindrome(s = "a.b,."))