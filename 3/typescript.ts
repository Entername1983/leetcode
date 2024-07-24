// Longest substring without rpeating characters

// Given a string s find the length of the longest substring without repeating characters.

function lengthOfLongestSubstring(s: string): number {
  let length = 1;
  const sList: string[] = s.split("");
  let seenChars = new Map<string, number>();
  let i = 0;
  while (i < sList.length) {
    if (seenChars.has(sList[i])) {
      if (seenChars.size > length) {
        length = seenChars.size;
      }
      i = Number(seenChars.get(sList[i])) + 1;
      seenChars.clear();
    } else {
      seenChars.set(sList[i], Number(i));
      if (seenChars.size > length) {
        length = seenChars.size;
      }
      i++;
    }
  }
  return Math.min(length, sList.length);
}

console.log(lengthOfLongestSubstring("dvdf"));

// function lengthOfLongestSubstring(s: string): number {
//     let map = new Map<string, number>();
//     let maxLen = 0;
//     let left = 0;
//     for (let right = 0; right < s.length; right++) {
//         if (map.has(s[right])) {
//             left = Math.max(map.get(s[right])!, left);
//         }
//         maxLen = Math.max(maxLen, right - left + 1);
//         map.set(s[right], right + 1);
//     }
//     return maxLen;
// };
