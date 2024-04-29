function findNeedle(haystack) {
  let position = haystack.indexOf('needle')
    return `found the needle at position ${position}`;
}

/* Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2] */

function powersOfTwo(n){
    const powers = [];
    for (let i = 0; i <= n; i++) {
        powers.push(2**i)
    }
  return powers
}

// const result = powersOfTwo(5);
// console.log(result);

// Given a number n, return the number of positive odd numbers below n, EASY!
// Examples (Input -> Output)
// 7  -> 3 (because odd numbers below 7 are [1, 3, 5])
// 15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])

function oddCount(n){
  return Math.floor(n/2)
}

// const result = oddCount(11);
// console.log(result);

// Create a function which checks a number for three different properties.
//
//     is the number prime?
//     is the number even?
//     is the number a multiple of 10?
//
// Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.
// Examples
//
// numberProperty(7)  // ==> [true,  false, false]
// numberProperty(10) // ==> [false, true,  true]
//
// The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:
//
// numberProperty(-7)  // ==> [false, false, false]
// numberProperty(-10) // ==> [false, true,  true]

function numberProperty(n) {
const lst = [];
const prime = [];
    if (n <= 1) {
        lst.push(false);
    }
        else{
            for (let i = 2; i < n; i++) {
                if (n % i === 0) {
                    prime.push(false);
                }
            }
            if (prime.includes(false)) {
                lst.push(false);
            } else {
                lst.push(true);
            }
        }
    lst.push(n % 2 === 0);
    lst.push(n % 10 === 0);
    return lst
}

// works but get timed out...
// const result = numberProperty(-10);
// const result1 = numberProperty(131);
// console.log(result);
// console.log(result1);