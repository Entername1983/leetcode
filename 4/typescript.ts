// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const fullArray = [...nums1, ...nums2];
  const fullArrayLength = fullArray.length;
  const isEven = !(fullArrayLength % 2);
  const sortedArray = fullArray.sort((a, b) => a - b);
  console.log("sortedArray", sortedArray);
  const halfwayPoint = fullArrayLength / 2;
  if (!isEven) {
    return sortedArray[halfwayPoint - 0.5];
  }
  return (sortedArray[halfwayPoint - 1] + sortedArray[halfwayPoint]) / 2;
}

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const lengthNums1 = nums1.length;
  const lengthNums2 = nums2.length;
  const totalLength = lengthNums1 + lengthNums2;
  const isEven = !(totalLength % 2);
  const adjustor = isEven ? 1 : 0;
  let i = 0;
  let i1 = 0;
  let i2 = 0;
  let medianNumber = 0;
  const halfwayPoint = Math.ceil(totalLength / 2) - 1;
  while (i <= halfwayPoint + adjustor) {
    console.log("i", i, "i1", i1, "i2", i2);
    const val1 = nums1[i1] ?? Infinity;
    const val2 = nums2[i2] ?? Infinity;

    if (val1 < val2) {
      if (i >= halfwayPoint) {
        medianNumber += val1;
      }
      i1++;
    } else {
      if (i >= halfwayPoint) {
        medianNumber += val2;
      }
      i2++;
    }
    i++;
  }
  return !isEven ? medianNumber : medianNumber / 2;
}
console.log(findMedianSortedArrays([1, 3], [2]));
console.log("-------------");
console.log(findMedianSortedArrays([1, 2], [3, 4]));
console.log("-------------");
console.log(findMedianSortedArrays([3], [-2, -1]));

//look at first number in first list.  Is it bigger than first number in second list
//no, put it in new list, pop it
