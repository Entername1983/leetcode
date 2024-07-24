// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).
// function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
//   const fullArray = [...nums1, ...nums2];
//   const fullArrayLength = fullArray.length;
//   const isEven = !(fullArrayLength % 2);
//   const sortedArray = fullArray.sort((a, b) => a - b);
//   console.log("sortedArray", sortedArray);
//   const halfwayPoint = fullArrayLength / 2;
//   if (!isEven) {
//     return sortedArray[halfwayPoint - 0.5];
//   }
//   return (sortedArray[halfwayPoint - 1] + sortedArray[halfwayPoint]) / 2;
// }
function findMedianSortedArrays(nums1, nums2) {
    var _a, _b;
    var lengthNums1 = nums1.length;
    var lengthNums2 = nums2.length;
    var totalLength = lengthNums1 + lengthNums2;
    var isEven = !(totalLength % 2);
    var adjustor = isEven ? 1 : 0;
    var i = 0;
    var i1 = 0;
    var i2 = 0;
    var medianNumber = 0;
    var halfwayPoint = Math.ceil(totalLength / 2) - 1;
    console.log("halfway point", halfwayPoint);
    // keep going through a loop until we reach the halfway point
    // for an even list we want to get (index[length/2 - 1] + index[length/2]) / 2 --> so want to keep going until i >= length/2
    // for an odd list we want to get median number index[length/2 - 0.5] --> so we want to keep going until i >= length/2 -0.5
    while (i <= halfwayPoint + adjustor) {
        console.log("i", i, "i1", i1, "i2", i2);
        var val1 = (_a = nums1[i1]) !== null && _a !== void 0 ? _a : Infinity;
        var val2 = (_b = nums2[i2]) !== null && _b !== void 0 ? _b : Infinity;
        if (val1 < val2) {
            if (i >= halfwayPoint) {
                console.log("adding val1", val1);
                medianNumber += val1;
            }
            i1++;
        }
        else {
            if (i >= halfwayPoint) {
                console.log("adding val2", val2);
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
