"""Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
Converting a decimal place value into a Roman numeral has the following rules:

1- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
2- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used:
4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
3- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form."""

## create a mapping of ints to numerals for lookup

RomanDict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

## Create a seperate mapping for 4's and 9s?  Or add them to existing mapping

## Start from left to right or right to left

## example, 58 = "LVIII"
NUMBER = 58
n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
def int_to_roman(num):
    answer = []
    i = 0
    while num > 0:
        print(f"i is {i}")
        if (num >=n[i]):
            answer.append(s[i])
            print(num)
            num -= n[i]
            print(answer)
        else:
            i += 1
    print(answer)
    return "".join(answer)

int_to_roman(NUMBER)



# End-of-file (EOF)