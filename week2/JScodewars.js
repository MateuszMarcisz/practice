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

function numberProperty(n)
// {
// const lst = [];
// const prime = [];
//     if (n <= 1) {
//         lst.push(false);
//     } else{
//         for (let i = 2; i < n; i++) {
//                 if (n % i === 0) {
//                     prime.push(false);
//                 }
//             }
//             if (prime.includes(false)) {
//                 lst.push(false);
//             } else {
//                 lst.push(true);
//             }
//         }
//     lst.push(n % 2 === 0);
//     lst.push(n % 10 === 0);
//     return lst
// }
{const lst = [];
    if (n <= 1) {
        lst.push(false);
    } else{
        let prime = true
        for (let i = 2; i < n; i++) {
                if (n % i === 0) {
                    prime = false;
                    break;
                }
            }
            if (prime === false) {
                lst.push(false);
            } else {
                lst.push(true);
            }
        }
    lst.push(n % 2 === 0);
    lst.push(n % 10 === 0);
    return lst
}

// works but get timed out... not its fixed, most important was adding break to the prime loop
// const result = numberProperty(-10);
// const result1 = numberProperty(341);
// console.log(result);
// console.log(result1);

// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
function evenOrOdd(number) {
  if (number % 2 === 0) {
      return 'Even'
  } else {
      return 'Odd'
  }
}

// Return the number (count) of vowels in the given string.
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
    let count = 0
    for (let vowel of str){
        if (('aeiou').includes(vowel)) {
        count += 1
  }
    }
    return count
}

// Trolls are attacking your comment section!
// A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
// Your task is to write a function that takes a string and return a new string with all vowels removed.
// For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
// Note: for this kata y isn't considered a vowel.
function disemvowel(str) {
    let words = "";
    for (let letter of str){
        if (('aeiouAEIOU').includes(letter)){
            words += "";
        } else {
            words += letter;
        }
    }
    return words;
}

// const result = disemvowel("This website is for losers LOL!");
// console.log(result);

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Additionally, if the number is negative, return 0.
// Note: If the number is a multiple of both 3 and 5, only count it once.
// Courtesy of projecteuler.net (Problem 1)

function solution(number){
 if (number === 0) {
     return 0;
 } else {
     let numbers = [];
     for (let i = 1; i < number; i++) {
         if (i % 3 === 0 || i % 5 === 0) {
             numbers.push(i)
         }
     }
     return (numbers).reduce((a, b) => a + b, 0);
 }
}
// const result = solution(10);
// console.log(result);

// Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
// For example,
// [true,  true,  true,  false,
//   true,  true,  true,  true ,
//   true,  false, true,  false,
//   true,  false, false, true ,
//   true,  true,  true,  true ,
//   false, false, true,  true]
// The correct answer would be 17.
function countSheeps(sheep) {
    return sheep.filter(i => i === true).length;
}
// const result = countSheeps([true,  true,  true,  false,
//   true,  true,  true,  true ,
//   true,  false, true,  false,
//   true,  false, false, true ,
//   true,  true,  true,  true ,
//   false, false, true,  true]);
// console.log(result);


function squareDigits(num){
    let numberz = [];
    for (let i of num.toString()) {
      numberz.push(i**2);
    }
    return Number(numberz.join(''));
}

// let result = squareDigits(3212)
// console.log(result)
// let result1 = squareDigits(2112)
// console.log((result1))

function highAndLow(numbers){
    let numberz = numbers.split(' ').map(Number);
    let nums = numberz.sort((a,b) => a -b);
    let num1 = nums[0];
    let num2 = nums[nums.length -1];
    return `${num2} ${num1}`
}


function descendingOrder(n){
    const nums = n.toString().split('')
    return Number(nums.sort((a,b) => b-a).join(''))
}


let result = descendingOrder(123456789)
let result1 = descendingOrder(105654)
console.log((result1))