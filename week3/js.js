// An isogram is a word that has no repeating letters, consecutive or non-consecutive.
// Implement a function that determines whether a string that contains only letters is an isogram.
// Assume the empty string is an isogram. Ignore letter case.
// Example: (Input --> Output)
// "Dermatoglyphics" --> true
// "aba" --> false
// "moOse" --> false (ignore letter case)



function isIsogram(str){
    let lst1 = [];
    let lst2 = [];
    str = str.toLowerCase()
    for (let i of str){
        lst1.push(i);
        if (!(lst2.includes(i))){
            lst2.push(i);
        }
    } return lst1.toString() === lst2.toString();
}

// result = isIsogram('Dermatoglyphics');
// console.log(result);
// result1 = isIsogram('aba');
// console.log(result1);
// result2 = isIsogram('moOse');
// console.log(result2);

// Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with
// all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
// If the number is prime return the string '(integer) is prime'
// Example:
//
// divisors(12); // should return [2,3,4,6]
// divisors(25); // should return [5]
// divisors(13); // should return "13 is prime"


function divisors(integer) {
    const lst = [];
    for (let i = 1; i <=integer; i++){
        if (integer % i === 0){
            lst.push(i);
        }
    }
if (lst.length === 2){
    return `${integer} is prime`
}
return lst.slice(1,lst.length-1);
}


// x1 = divisors(12);
// x2 = divisors(25);
// x3 = divisors(13);
// console.log(x1);
// console.log(x2);
// console.log(x3);

function drawStairs(n) {
    let stairs = 'I';
    for (let i = 2; i<=n;i++){
        stairs += '\n'
        stairs += ' '.repeat(i-1);
        stairs += 'I';
    }
return stairs
}

// x1 = drawStairs(1);
// console.log(x1);
// x2 = drawStairs(4);
// console.log(x2);
// x3 = drawStairs(7);
// console.log(x3);

// I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.
//
// P.S. Each array includes only integer numbers. Output is a number too.

function arrayPlusArray(arr1, arr2) {
  arr1.push(...arr2);
  return arr1.reduce((a,b)=>a+b);
}


// x1 = arrayPlusArray([1, 2, 3], [4, 5, 6]);
// console.log(x1);

// Find the difference between two collections. The difference means that either the character is present in one collection or it is present in other,
// but not in both. Return a sorted list with the difference.
// The collections can contain any character and can contain duplicates.
// Example
// A = [a, a, t, e, f, i, j]
// B = [t, g, g, i, k, f]
// difference = [a, e, g, j, k]

function diff(a, b){
    let difference = [];
    for (let i of a){
        if(!(b.includes(i)) && !(difference.includes(i))){
            difference.push(i)
        }
    } for (let i of b) {
        if (!(a.includes(i)) && !(difference.includes(i))) {
            difference.push(i)
        }
    }
  return difference
}

// x1 = diff(['a', 'a', 't', 'e', 'f', 'i', 'j'], ['t', 'g', 'g', 'i', 'k', 'f']);
// console.log(x1);

// Task
// Given a string, return if all occurrences of a given letter are always immediately followed by the other given letter.
// Worked Example
// ("he headed to the store", "h", "e") ➞ True
// # All occurences of "h": ["he", "headed", "the"]
// # All occurences of "h" have an "e" after it.
// # Return True
// ('abcdee', 'e', 'e') ➞ False
// # For first "e" we can get "ee"
// # For second "e" we cannot have "ee"
// # Return False
// Examples
// ("i found an ounce with my hound", "o", "u") ➞ True
// ("we found your dynamite", "d", "y") ➞ False

function bestFriend(txt, a, b) {
    for (let i = 0; i <txt.length;i++){
        if (txt[i] === a && txt[i+1] !== b){
            return false
        }
    }
return true
}

// x1 = bestFriend("we found your dynamite", "d", "y");
// x2 = bestFriend("i found an ounce with my hound", "o", "u");
// console.log(x1);
// console.log(x2);