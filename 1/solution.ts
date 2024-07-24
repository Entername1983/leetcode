// Looking for a target, we can utilize some elementary alegbra...
// By subtracting the value we're looping over from the target number, we
// find what value needs to be added onto the looped number in order equal the target.
// If this calculated difference exists in a map (used for value => index storage)
// we can retrieve its index, and pair it with the index of the value being looped over
// to successfully complete the problem

function twoSum(numbers: number[], target: number): number[] {
  // create a map as a method of key value storage for O(1) search / access
  // Array has an O(n) search-time, so we opt for the map
  const numberMap = new Map();

  // start by looping through each number (we use a traditional
  // for-loop here since it allows us to use "break" or "return" if we find
  // the number we're looking for before reaching the end of the array)
  for (let i = 0; i < numbers.length; i++) {
    const number = numbers[i];

    // here we find the difference between the target and number...
    // "difference" represents the number that needs to be added
    // onto "number" (the current number we're looping over) in order
    // to equal the function's target number
    const difference = target - number;

    // check numberMap for the difference value. if we already
    // looped over this number, that means it's in our map, therefore
    // we can retrieve the value from our map (O(1)), get its index, and return
    // the index we're currently looping over to complete the problem
    if (numberMap.has(difference)) return [numberMap.get(difference), i];

    // if we haven't already looped over the number, store it
    // and its index in a JS Map (hash table) so we can
    // get an O(1) search / access check to see if we looped over the
    // number previously
    numberMap.set(number, i);
  }
}
