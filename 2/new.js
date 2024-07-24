var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
    return ListNode;
}());
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
var l1 = [2, 4, 3];
var l2 = [5, 6, 4];
function addTwoNumbers(l1, l2) {
    return addNode(l1, l2, null, 0);
}
function addNode(l1, l2, prevNode, linkedList, carryOver) {
    if (carryOver === void 0) { carryOver = 0; }
    console.log("entering addNode");
    // if l1.next === null & l2.next === null
    var newCarry = 0;
    var newNum = 0;
    if (l1 === null && l2 === null) {
        if (prevNode === null) {
            return null;
        }
        prevNode.next = null;
        console.log("returning", linkedList);
        return linkedList;
    }
    else {
        var lOneVal = (l1 === null || l1 === void 0 ? void 0 : l1.val) || 0;
        var lTwoVal = (l2 === null || l2 === void 0 ? void 0 : l2.val) || 0;
        var valSum = lOneVal + lTwoVal + carryOver;
        if (valSum >= 10) {
            newNum = valSum - 10;
            newCarry = 1;
        }
        else {
            newNum = valSum;
        }
        // create new node and add it
        // creating new node
        var newNode = new ListNode();
        newNode.val = newNum;
        var initialList = void 0;
        if (prevNode !== null) {
            prevNode.next = newNode;
            initialList = linkedList;
        }
        else {
            initialList = newNode;
        }
        return addNode((l1 === null || l1 === void 0 ? void 0 : l1.next) || null, (l2 === null || l2 === void 0 ? void 0 : l2.next) || null, newNode, initialList, newCarry);
    }
}
// add the values together, initailize new node
// set new node as next of previous one
// if values are null set next as null and return list node
console.log(addTwoNumbers(arrayToListNode(l1), arrayToListNode(l2)));
