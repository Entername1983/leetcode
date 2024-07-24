// GIven a string s, return the longest palindromic substring in s
// take the first letter, compare it to the next letter, check lnegth, if longer than saved palindrome replace it with current
// repeat for
// edge case is something like abc, only single letter palindromes (does that count?)

// function arraysEqual(a: any[], b: any[]): boolean {
//   return a.length === b.length && a.every((val, index) => val === b[index]);
// }

// function longestPalindrome(s: string): string {
//   let sList = s.split(""); // split string to list to make it easier to work with
//   const sLength = sList.length;
//   if (sLength == 1) {
//     // if length is 1 then the palindrome is simply one letter
//     return s;
//   }
//   // loop through the list, every time incrementing start pointer by 1, continue we are sure to have found the longest palindrome --> sLength - length of max stored palindrome (because not enough letters to make one longer)

//   // inner loop incrementing end pointer by 1
//   // 2 cases middle letter is doubled, middle letter is singletgon
//   // slice the list from start and end point <-- list 1
//   // slice the list from end + 1 and end + 1 + list 1 length + reverse it <-- list 2
//   // if list 1 = list 2 --> palindrome --> store it + store max length and increment start.  Otherwise check for list 3
//   // slice the list from end and end + list length + reverse it <-- list 3
//   let palList: string[] = [];
//   let start: number = 0;
//   let end: number = 0;
//   let maxLength = 0;
//   for (start; start <= sLength - 1 - maxLength; start++) {
//     end = start;
//     while (end <= sLength - 1) {
//       if (end - start >= (maxLength - 1) / 2) {
//         // check if there is a possibility that this palindrome exceeeds the existing max length one first
//         const list1 = sList.slice(start, end + 1);
//         const list1Length = list1.length;
//         const list2 = sList.slice(end + 1, end + 1 + list1Length);
//         const list2Rev = list2.slice().reverse();
//         if (arraysEqual(list1, list2Rev)) {
//           palList = [...list1, ...list2];
//           maxLength = list1Length * 2;
//         } else {
//           const list3 = sList.slice(end, end + list1Length);
//           const list3Rev = list3.slice().reverse();
//           if (arraysEqual(list1, list3Rev)) {
//             list3.shift();
//             palList = [...list1, ...list3];
//             maxLength = list1Length * 2 - 1;
//           }
//         }
//       }
//       end++;
//     }
//   }
//   const joinedList = palList.join("");
//   return joinedList;
// }

// function longestPalindrome(s: string): string {
//   let sList = s.split("");
//   console.log("string", s);
//   //start on first letter.  Compare it to last letter.  If not the same --> not a palindrome, reset
//   // if is the same, check the next letter

//   let start: number = 0;
//   const sLength: number = sList.length;
//   console.log("sLength", sLength);
//   let maxLength: number = 0;
//   let palList: string[] = [];
//   let startCurrent: number = 0; // tracking the beginning of the current string we are working on
//   let endCurrent: number = 0; // tracking the end of the current string we are working on
//   // should only keep going while it still possible to form a longer palindrome
//   let firstIndex = start; // index of first char to comprae
//   let secondIndex = sLength - 1; // index of 2nd char to compare

//   while (start < sLength - 1) {
//     // there should be more chars left than the max length palindrome found
//     while (secondIndex >= firstIndex) {
//       console.log("firstIndex", firstIndex, "secondIndex", secondIndex);
//       console.log(
//         "first char",
//         sList[firstIndex],
//         "secondChar",
//         sList[secondIndex]
//       );
//       if (sList[firstIndex] === sList[secondIndex]) {
//         // chars are the same we shoudl continue checking
//         //check if we have reached the middle --> the end
//         if (firstIndex == secondIndex || firstIndex == secondIndex + 1) {
//           console.log("found middle");
//           const workingList = sList.slice(startCurrent, endCurrent + 1);
//           if (workingList.length > maxLength) {
//             palList = workingList;
//             maxLength = workingList.length;
//             firstIndex += 1;
//             secondIndex -= 1;
//           }
//         } else {
//           firstIndex += 1;
//           secondIndex -= 1;
//         }
//       } else {
//         secondIndex--;
//         endCurrent = secondIndex;
//       }
//     }
//     start++;
//     firstIndex = start;
//     startCurrent = firstIndex;
//   }
//   console.log("maxLengt", maxLength);
//   console.log("start", start);
//   console.log("sLength", sLength);
//   return palList.join("");
// }

// function longestPalindrome(s: string): string {
//   const sList = s.split("");
//   const sListLength = sList.length;
//   let longestList: string[] = [];
//   if (sListLength == 1) {
//     return s;
//   }

//   // loop through each item in the list
//   // list within al ist
//   let maxLength = 0;
//   let i = 0;
//   let startIndex: number = 0;
//   let endIndex: number = 0;
//   for (i; i < sListLength - 1; i++) {
//     if (sListLength - i < maxLength) {
//       break;
//     }
//     let j = 1;
//     for (j; j <= sListLength - (i + 1); j++) {
//       console.log("i", i, "j", j);
//       //   if (j - i >= maxLength) {
//       let tempStart = i;
//       let tempEnd = sListLength - j;
//       console.log("tempStart", tempStart);
//       console.log("tempEnd", tempEnd);
//       // char i = char j
//       // continue current palindrome
//       // compare char i + 1, char j - 1
//       if (sList[tempStart] === sList[tempEnd]) {
//         console.log("EQUAL tempStart", tempStart, "tempEnd", tempEnd);
//         console.log("maxLength", maxLength);
//         if (tempStart == tempEnd && tempEnd - tempStart > maxLength) {
//           longestList = sList.slice(startIndex, endIndex + 1);
//           maxLength = tempEnd - tempStart;
//         }
//         if (tempEnd - tempStart > maxLength) {
//           console.log("setting start index", startIndex, "endIndex,", tempEnd);
//           startIndex = tempStart;
//           endIndex = tempEnd;
//           maxLength = tempEnd - tempStart;
//         }

//         tempStart++;
//         //   if (tempStart === tempEnd) {
//         //     console.log("found the middle");
//         //     maxLength = endIndex - startIndex;
//         //   }
//         // }
//       }

//       // char i not char j
//       // reset working palindrome
//       // compare char i char j - 1
//     }
//   }
//   return sList.slice(startIndex, endIndex + 1).join("");
// }

// // checks if the piece of a list is a palindrome, returns true if it is
// function checkPal(startIndex, endIndex, sList): boolean {
//   if (sList[startIndex] === sList[endIndex]) {
//     if ((startIndex = endIndex)) {
//       return true;
//     } else {
//       return checkPal(startIndex + 1, endIndex - 1, sList);
//     }
//   }
//   return false;
// }

function checkPal(startIndex, endIndex, sList): boolean {
  if (sList[startIndex] === sList[endIndex]) {
    if (startIndex === endIndex || endIndex - startIndex === 1) {
      return true;
    } else {
      return checkPal(startIndex + 1, endIndex - 1, sList);
    }
  }
  return false;
}

function longestPalindrome(s: string): string {
  const sListLength = s.length;
  if (sListLength == 1) {
    return s;
  }
  let maxLength = 0;
  let longestStart: number = 0;
  let longestEnd: number = 0;
  let i = 0;
  for (i; i < sListLength - 1; i++) {
    if (maxLength > sListLength - i) {
      break;
    }
    let j = sListLength - 1;
    while (i <= j) {
      if (j - i >= maxLength) {
        if (checkPal(i, j, s)) {
          longestStart = i;
          longestEnd = j + 1;
          maxLength = j - i;
        }
      }
      j--;
    }
  }
  return s.substring(longestStart, longestEnd);
}

console.log("abb ==", longestPalindrome("abb"));
console.log(
  "Super long one == ",
  longestPalindrome(
    "dtgrtoxuybwyfskikukcqlvprfipgaygawcqnfhpxoifwgpnzjfdnhpgmsoqzlpsaxmeswlhzdxoxobxysgmpkhcylvqlzenzhzhnakctrliyyngrquiuvhpcrnccapuuwrrdufwwungaevzkvwbkcietiqsxpvaaowrteqgkvovcoqumgrlsxvouaqzwaylehybqchsgpzbkfugujrostopwhtgrnrggocprnxwsecmvofawkkpjvcchtxixjtrnngrzqpiwywmnbdnjwqpmnifdiwzpmabosrmzhgdwgcgidmubywsnshcgcrawjvfiuxzyzxsbpfhzpfkjqcpfyynlpshzqectcnltfimkukopjzzmlfkwlgbzftsddnxrjootpdhjehaafudkkffmcnimnfzzjjlggzvqozcumjyazchjkspdlmifvsciqzgcbehqvrwjkusapzzxyiwxlcwpzvdsyqcfnguoidiiekwcjdvbxjvgwgcjcmjwbizhhcgirebhsplioytrgjqwrpwdciaeizxssedsylptffwhnedriqozvfcnsmxmdxdtflwjvrvmyausnzlrgcchmyrgvazjqmvttabnhffoe"
  )
);
console.log("cbbd == ", longestPalindrome("ccbbcd"));
console.log("aca== ", longestPalindrome("baaca"));
