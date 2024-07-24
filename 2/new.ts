class ListNode {
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

const l1 = [2, 4, 3];
const l2 = [5, 6, 4];

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  return addNode(l1, l2, null, null, 0);
}

function addNode(
  l1: ListNode | null,
  l2: ListNode | null,
  prevNode: ListNode | null,
  linkedList: ListNode | null,
  carryOver: number = 0
): ListNode | null {
  // if l1.next === null & l2.next === null
  let newCarry = 0;
  let newNum = 0;
  if (l1 === null && l2 === null) {
    if (prevNode === null) {
      return null;
    }
    if (carryOver === 1) {
      const lastNode = new ListNode(1, null);
      prevNode.next = lastNode;
    } else {
      prevNode.next = null;
    }
    return linkedList;
  } else {
    const lOneVal = l1?.val || 0;
    const lTwoVal = l2?.val || 0;
    const valSum = lOneVal + lTwoVal + carryOver;
    if (valSum >= 10) {
      newNum = valSum - 10;
      newCarry = 1;
    } else {
      newNum = valSum;
    }

    let newNode = new ListNode(newNum);
    let initialList;
    if (prevNode !== null) {
      prevNode.next = newNode;
      initialList = linkedList;
    } else {
      initialList = newNode;
    }

    return addNode(
      l1?.next || null,
      l2?.next || null,
      newNode,
      initialList,
      newCarry
    );
  }
}

// add the values together, initailize new node
// set new node as next of previous one
// if values are null set next as null and return list node

console.log(addTwoNumbers(arrayToListNode(l1), arrayToListNode(l2)));

// function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
//   const result = new ListNode();
//   let current = result;
//   let carry = 0;

//   while (l1 !== null || l2 !== null) {
//     let sum = carry;
//     if (l1 !== null) {
//       sum += l1.val;
//       l1 = l1.next;
//     }

//     if (l2 !== null) {
//       sum += l2.val;
//       l2 = l2.next;
//     }

//     current.next = new ListNode(sum % 10);
//     carry = Math.floor(sum / 10);
//     current = current.next;
//   }

//   if (carry !== 0) current.next = new ListNode(carry);

//   return result.next;
