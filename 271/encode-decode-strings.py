
## UTF 8 --> 256 characters
## chr() to turn it back into a char, ord() to turn it into unicode
## take the unicode value, add 10 to it
## going to need to have a way to delineate between strings.  let's say ^^^^

DELIMITER: list[str] = ["^" ,"_", "^", "_"]
ENC_DEL: list[str] = ["c", "d", "c", "d"]
ADJUSTOR: int = 5
TOTAL_UTF8: int = 256



def encode(strs: list[str]) -> str:
    print(ord(" "))
    if strs == [""]:
        return "--null--string--"
    if strs == []:
        return "--null--"
    new_str_list: list[str] = []
    for s in strs:
        s_list = list(s)
        print(s)
        s_list += DELIMITER
        for c in s_list:
            encoded_char = chr(ord(c) + ADJUSTOR % TOTAL_UTF8)
            new_str_list.append(encoded_char)
    return "".join(new_str_list)

def decode(s: str) -> list[str]:
    if s == "--null--":
        return []
    if s == "--null--string--":
        return [""]
    s_list: list[str] = list(s)
    i = 0
    n: int = len(s_list)
    answer_list: list[list[str]] = [[]]
    j: int = 0 ## index for lists within answer list
    while i < n:
        ## decode individual character
        decoded_char = chr((ord(s_list[i]) - ADJUSTOR) % 256)
        if decoded_char == DELIMITER[0] and i + 3 <= n and s_list[i:i+4] == ENC_DEL:
            i += 3
            j += 1
            answer_list.append([])
        else:
            answer_list[j].append(decoded_char)
        i+=1
    final_list: list[str] = []
    for _, value in enumerate(answer_list):
        if len(value) != 0:
            joined_str = "".join(value)
            final_list.append(joined_str)
    return final_list
# print(encode(strs=[""]))
# print(decode(encode(strs=[""])))


# print("Encoding", ["I", "Love", "Silvana"])
# print(encode(strs=["I", "Love", "Silvana"]))

# print("---------------------------")

# print("Decoding ", encode(strs=["I", "Love", "Silvana"]))
# print(decode(encode(strs=["I", "Love", "Silvana"])))


# ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]

print("Decoding ", encode(strs=["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
))
