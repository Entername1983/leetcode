
## "III" == 3
## "LVIII" == 58

## if I --> check if next is V or X
## if X check if next is L or C
## if C check if next is 500 or 1000

## if a number repeats itself --> multiply it by the number of occurances
##


ROMAN_DICT = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
DOUBLE_DICT = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

def roman_to_int(s: str) -> int:
    print("calling roman to int")
    i: int = 0
    answer: int = 0
    print(i)
    
    while i < len(s):
        single: str = s[i]
        if (i+1 < len(s)) and (s[i]+s[i+1] in DOUBLE_DICT):
            answer += DOUBLE_DICT[s[i]+s[i+1]]
            i += 2
        else:
            answer += ROMAN_DICT[single]
            i += 1
        print(answer)
    print(f"Answer {answer}")
    return answer

roman_to_int("MCDLXXVI")