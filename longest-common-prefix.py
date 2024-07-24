

def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    longest_prefix: list = []
    shortest_string: str = min(strs, key = len)
    i: int = 0
    while i < len(shortest_string):
        for string in strs:
            if string[i] != shortest_string[i]:
                return "".join(longest_prefix)
        longest_prefix.append(shortest_string[i])
        i += 1
    return "".join(longest_prefix)


longestCommonPrefix(["flower","flow","flight"])