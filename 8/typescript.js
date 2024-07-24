var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function myAtoi(s) {
    var newNumber = [];
    var numberEntered = false;
    var posNumber = true;
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var c = s_1[_i];
        if (c === " ") {
            if (numberEntered) {
                return checkAndReturn(posNumber, newNumber);
            }
            continue;
        }
        if (Number.isNaN(Number(c))) {
            switch (c) {
                case "+":
                    if (numberEntered) {
                        return checkAndReturn(posNumber, newNumber);
                    }
                    posNumber = true;
                    numberEntered = true;
                    break;
                case "-":
                    if (numberEntered) {
                        return checkAndReturn(posNumber, newNumber);
                    }
                    posNumber = false;
                    numberEntered = true;
                    break;
                default:
                    if ((numberEntered = true)) {
                        return checkAndReturn(posNumber, newNumber);
                    }
                    break;
            }
        }
        else {
            newNumber = __spreadArray(__spreadArray([], newNumber, true), [c], false);
            numberEntered = true;
        }
    }
    return checkAndReturn(posNumber, newNumber);
}
function checkAndReturn(posNumber, newNumber) {
    var numToReturn = Number(newNumber.join(""));
    if (numToReturn >= Math.pow(2, 31)) {
        if (posNumber) {
            return Math.pow(2, 31) - 1;
        }
        else {
            return -(Math.pow(2, 31));
        }
    }
    return posNumber ? numToReturn : numToReturn * -1;
}
console.log(myAtoi("   +0 123"));
21474836460;
2147483648;
