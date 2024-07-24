function singleNumber(nums: number[]): number {
  let seenNumbers: { [key: number]: number } = {};
  for (let i of nums) {
    if (i in seenNumbers) {
      seenNumbers[i] += 1;
    } else {
      seenNumbers[i] = 1;
    }
  }
  for (let i in seenNumbers) {
    if (seenNumbers[i] === 1) {
      return Number(i);
    }
  }
  return 0;
}

console.log(singleNumber([4, 1, 2, 1, 2]));
