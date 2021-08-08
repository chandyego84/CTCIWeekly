// Filter can be applied on an array based on a condition.
// Calls a function on each element of a collection (e.g., array)
// Thus, takes a function as parameter

let nums = [1, 2, 3, 6, 13, 21, 30, 42, 69]

// only makes list out of numbers whose value is < 20
const smallNums = nums.filter((elt) => elt < 20);
console.log(smallNums)