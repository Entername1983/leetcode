// return indicies of 2 numbers such that they add up to the target
// each input has exactly one solution, can not use the same element twice
function twoSum(nums, target) {
    console.log(nums);
    for (var i in nums) {
        console.log(i);
        for (var j = Number(i) + 1; j <= nums.length; j++) {
            console.log(j);
            console.log(nums[i], nums[j]);
            if (nums[i] + nums[j] === target) {
                console.log(i, j);
                return [Number(i), Number(j)];
            }
        }
    }
    return [0, 0];
}
twoSum([3, 2, 4], 6);
