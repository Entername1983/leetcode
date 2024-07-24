export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function arrayToListNode(numbers: number[]) {
  let dummyRoot = new ListNode(0);
  let ptr: ListNode | null = dummyRoot;
  for (let num of numbers) {
    ptr.next = new ListNode(num);
    ptr = ptr.next;
  }
  return dummyRoot.next;
}

function addTwoNumbers2(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  console.log(l1, l2);
  const l1List: number[] = getNumber(l1, []);
  const l2List: number[] = getNumber(l2, []);
  const l2Number: number = Number(l2List.join(""));
  const l1Number: number = Number(l1List.join(""));
  console.log("l1Num", l1Number, "l2Num", l2Number);

  const sumNumbers: number = l1Number + l2Number;
  console.log("sum of numbers", sumNumbers);
  const sumNumbersList: number[] = sumNumbers.toString().split("").map(Number);
  const result = arrayToListNode(sumNumbersList.reverse());
  console.log("result", result);
  return result;
}

function getNumber(l1: ListNode | null, numberList: number[]): number[] {
  let newList = numberList;
  if (l1) {
    newList = [...numberList, l1.val];
    return getNumber(l1.next, newList);
  } else {
    console.log("new list", newList);
    const reversedList = newList.reverse();

    return reversedList;
  }
}

const l1 = [9, 9, 9, 9, 9, 9, 9];
const l2 = [9, 9, 9, 9];

// Attempt 2
// retrieve a list from the linked list in reverse order
// find the longest list
// loop through the longest list starting at the end.  If hte lists are the same length just default ot eh first one
// add up the values of each item, + carry over from previous additions
// put them in a new list
// turn that list back into a linked list
function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const l1List: number[] = getNumber(l1, []);
  const l2List: number[] = getNumber(l2, []);
  console.log("l1List", l1List);
  console.log("l2List", l2List);
  const longestList = l1List.length >= l2List.length ? l1List : l2List;
  const otherList = longestList == l1List ? l2List : l1List;
  let carryOver = 0;
  let newList: number[] = [];
  for (let i = 0; i <= longestList.length - 1; i++) {
    const shortestListValue = otherList[otherList.length - 1 - i] | 0;
    let numberToAdd: number =
      longestList[longestList.length - 1 - i] + shortestListValue + carryOver;
    carryOver = 0;
    if (numberToAdd >= 10) {
      numberToAdd -= 10;
      carryOver += 1;
    }
    newList = [...newList, numberToAdd];
    if (i === longestList.length - 1) {
      if (carryOver !== 0) {
        newList = [...newList, carryOver];
      }
    }
  }
  const reversedList = newList.reverse();
  const result = arrayToListNode(reversedList);
  return result;
}

addTwoNumbers(arrayToListNode(l1), arrayToListNode(l2));
