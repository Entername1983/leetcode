// given an integer x, return true if x is a palindrome and false otherwise

function isPalindrome(x: number): boolean {
  const xString = String(x);
  let i = 0;
  const length = xString.length;
  while (i <= length / 2) {
    if (xString[i] !== xString[length - 1 - i]) {
      return false;
    }
    if (i === length - 1 - i || i === length - 2 - i) {
      return true;
    }
    i++;
  }
  return false;
}
