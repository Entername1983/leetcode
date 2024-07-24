// 10. Regular Expression Matching
// Hard
// Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
// '.' Matches any single character.​​​​
// '*' Matches zero or more of the preceding element.
// The matching should cover the entire input string (not partial).
// Example 1:
// Input: s = "aa", p = "a"
// Output: false
// Explanation: "a" does not match the entire string "aa".
// Example 2:
// Input: s = "aa", p = "a*"
// Output: true
// Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
// Example 3:
// Input: s = "ab", p = ".*"
// Output: true
// Explanation: ".*" means "zero or more (*) of any character (.)".
// Constraints:
// 1 <= s.length <= 20
// 1 <= p.length <= 20
// s contains only lowercase English letters.
// p contains only lowercase English letters, '.', and '*'.
// It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
//loop through string.
// Have an index for the pattern to show where we are at?
// * can represent more than one char!!! or none at all! <-- biggest difficulty
// Need to store previous char
// when replacing previous char if current char is * do not replace
function isMatch(s, p) {
    var prevChar;
    var sIndex = 0;
    var pIndex = 0;
    while (sIndex < s.length) {
        if (p[pIndex] !== ".") {
            if (p[pIndex] === "*") {
                console.log(s[sIndex]);
                console.log(prevChar);
                if (!(prevChar === s[sIndex] ||
                    prevChar === "." ||
                    prevChar === undefined)) {
                    console.log("false 1");
                    return false;
                }
            }
            else {
                if (!(s[sIndex] === p[pIndex])) {
                    console.log("false 2");
                    return false;
                }
                prevChar = p[pIndex];
            }
        }
        else {
            prevChar = s[sIndex];
        }
        sIndex++;
        pIndex++;
    }
    return true;
}
// console.log("false", isMatch("aa", "a"));
// console.log("true", isMatch("aa", "a*"));
console.log("true", isMatch("ab", ".*"));
// console.log("true", isMatch("abaa", "...*"));
// console.log("true", isMatch("abaa", "..*"));
// console.log("true", isMatch("abaa", "....*"));
