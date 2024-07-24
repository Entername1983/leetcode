function singleNumber(nums) {
    var seenNumbers = {};
    for (var _i = 0, nums_1 = nums; _i < nums_1.length; _i++) {
        var i = nums_1[_i];
        console.log(i);
        if (i in seenNumbers) {
            console.log(i, seenNumbers[i]);
            seenNumbers[i] += 1;
            console.log(seenNumbers);
        }
        else {
            seenNumbers[i] = 1;
        }
    }
    console.log(seenNumbers);
    for (var i in seenNumbers) {
        if (seenNumbers[i] === 1) {
            return Number(i);
        }
    }
    return 0;
}
console.log(singleNumber([4, 1, 2, 1, 2]));
