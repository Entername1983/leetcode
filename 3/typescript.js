// Longest substring without rpeating characters
// Given a string s find the length of the longest substring without repeating characters.
function lengthOfLongestSubstring(s) {
    var length = 1;
    var sList = s.split("");
    var seenChars = new Map();
    var i = 0;
    while (i < sList.length) {
        console.log(sList[i]);
        if (seenChars.has(sList[i])) {
            console.log("char has been seen", sList[i]);
            if (seenChars.size > length) {
                length = seenChars.size;
            }
            i = Number(seenChars.get(sList[i])) + 1;
            console.log("returning to position i", i);
            seenChars.clear();
        }
        else {
            seenChars.set(sList[i], Number(i));
            console.log("char has not been seen", sList[i]);
            if (seenChars.size > length) {
                length = seenChars.size;
            }
            i++;
        }
    }
    return Math.min(length, sList.length);
}
console.log(lengthOfLongestSubstring("dvdf"));
