// given an integer x, return true if x is a palindrome and false otherwise
function isPalindrome(x) {
    var xString = String(x);
    var i = 0;
    var length = xString.length;
    while (i <= length / 2) {
        console.log("xstring1", xString[i], "xstring2", xString[-i + 1]);
        if (xString[i] !== xString[length - 1 - i]) {
            return false;
        }
        if (i === length - 1 - i || i === length - 2 - i) {
            return true;
        }
        i++;
    }
}
console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
