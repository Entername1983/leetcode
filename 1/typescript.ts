// return indicies of 2 numbers such that they add up to the target
// each input has exactly one solution, can not use the same element twice

function twoSum(nums: number[], target: number): number[] {
  for (let i in nums) {
    for (let j = Number(i) + 1; j <= nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [Number(i), Number(j)];
      }
    }
  }
  return [0, 0];
}

twoSum([3, 2, 4], 6);
