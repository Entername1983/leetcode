"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ListNode = void 0;
var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
    return ListNode;
}());
exports.ListNode = ListNode;
function arrayToListNode(numbers) {
    var dummyRoot = new ListNode(0);
    var ptr = dummyRoot;
    for (var _i = 0, numbers_1 = numbers; _i < numbers_1.length; _i++) {
        var num = numbers_1[_i];
        ptr.next = new ListNode(num);
        ptr = ptr.next;
    }
    return dummyRoot.next;
}
function addTwoNumbers2(l1, l2) {
    console.log(l1, l2);
    var l1List = getNumber(l1, []);
    var l2List = getNumber(l2, []);
    var l2Number = Number(l2List.join(""));
    var l1Number = Number(l1List.join(""));
    console.log("l1Num", l1Number, "l2Num", l2Number);
    var sumNumbers = l1Number + l2Number;
    console.log("sum of numbers", sumNumbers);
    var sumNumbersList = sumNumbers.toString().split("").map(Number);
    var result = arrayToListNode(sumNumbersList.reverse());
    console.log("result", result);
    return result;
}
function getNumber(l1, numberList) {
    var newList = numberList;
    if (l1) {
        newList = __spreadArray(__spreadArray([], numberList, true), [l1.val], false);
        return getNumber(l1.next, newList);
    }
    else {
        console.log("new list", newList);
        var reversedList = newList.reverse();
        return reversedList;
    }
}
var l1 = [
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1,
];
var l2 = [5, 6, 4];
// Attempt 2
function addTwoNumbers(l1, l2) {
    // retrieve a list from the linked list in reverse order
    var l1List = getNumber(l1, []);
    var l2List = getNumber(l2, []);
    console.log("l1List", l1List);
    console.log("l2List", l2List);
    // find the longest list
    var longestList = l1List.length >= l2List.length ? l1List : l2List;
    var otherList = longestList == l1List ? l2List : l1List;
    console.log("longest list", longestList);
    // loop through the longest list starting at the end.  If hte lists are the same length just default ot eh first one
    var carryOver = 0;
    var newList = [];
    for (var i = 0; i <= longestList.length - 1; i++) {
        console.log("looping");
        console.log(i);
        var shortestListValue = otherList[otherList.length - 1 - i] | 0;
        var numberToAdd = longestList[longestList.length - 1 - i] + shortestListValue + carryOver;
        carryOver = 0;
        if (numberToAdd >= 10) {
            numberToAdd -= 10;
            carryOver += 1;
        }
        newList = __spreadArray(__spreadArray([], newList, true), [numberToAdd], false);
    }
    var reversedList = newList.reverse();
    console.log("reversedList", reversedList);
    var result = arrayToListNode(reversedList);
    console.log(result);
    return result;
    // add up the values of each item, + carry over from previous additions
    // put them in a new list
    // turn that list back into a linked list
}
addTwoNumbers(arrayToListNode(l1), arrayToListNode(l2));
