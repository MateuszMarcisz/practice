// Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy of it.
//// Note that you may have troubles if you do not return an actual copy, item by item, just a pointer or an alias for an existing list or array.
//// If not a list or array is given as a parameter in interpreted languages, the function should raise an error.
//// Examples:
//// t = [1, 2, 3, 4]
// tCopy = copyList(t)
// t[1] += 5
// t = [1, 7, 3, 4]
// tCopy = [1, 2, 3, 4]
function copyList(l){
  return l.slice()
}

// Your task is to write an update for a lottery machine. Its current version produces a sequence of random letters and integers (passed as a string to the function). Your code must filter out all letters and return unique integers as a string, in their order of first appearance. If there are no integers in the string return "One more run!"
// Examples
// "hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
// "ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
// "555"                   -->  "5"

function lottery(str){
  const lst = [];
for (let i of str){
  if (!isNaN(parseInt(i))){
    if (!lst.includes(i)) {
      lst.push(i);
    }
  }
}
if (lst.length === 0){
  return "One more run!"
}
return lst.join('');
}

// x1 = lottery('hPrBKWDH8yc6Lt5NQZWQ');
// console.log(x1);
// x2 = lottery('555');
// console.log(x2);
// x3 = lottery("ynMAisVpHEqpqHBqTrwH");
// console.log(x3);


// You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
//
// Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
//
// []                                -->  "no one likes this"
// ["Peter"]                         -->  "Peter likes this"
// ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
// ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
// ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
//
// Note: For 4 or more names, the number in "and 2 others" simply increases.

function likes(names) {
  switch (names.length){
    case 0:
      return 'no one likes this';
    case 1:
      return `${names[0]} likes this`;
    case 2:
      return `${names[0]} and ${names[1]} like this`;
    case 3:
      return `${names[0]}, ${names[1]} and ${names[2]} like this`;
    default:
      return `${names[0]}, ${names[1]} and ${names.length-2} others like this`;
  }
}

// const x0 = likes([])
// console.log(x0);
// const x1 = likes(["Max"])
// console.log(x1);
// const x2 = likes(["Max", "John"])
// console.log(x2);
// const x3 = likes(["Max", "John", "Mark"])
// console.log(x3);
// const x4 = likes(["Alex", "Jacob", "Mark", "Max"]);
// console.log(x4);

// Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
// If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
// Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

function lovefunc(flower1, flower2){
  return (flower1 % 2 === 0 && flower2 % 2 === 1) || (flower1 % 2 === 1 && flower2 % 2 === 0);
}
//
// const x0 = lovefunc(2,6)
// const x1 = lovefunc(2,5)
// console.log(x0);
// console.log(x1);

// Clock shows h hours, m minutes and s seconds after midnight.
//
// Your task is to write a function which returns the time since midnight in milliseconds.
// Example:
//
// h = 0
// m = 1
// s = 1
//
// result = 61000
//
// Input constraints:
//
//     0 <= h <= 23
//     0 <= m <= 59
//     0 <= s <= 59

function past(h, m, s){
return 3600000 * h + 60000 * m + 1000 * s
}

// const x0 = past(0,1,1);
// const x1 = past(1,1,1);
// const x2 = past(0,0,0);
// const x3 = past(1,0,1);
// console.log(x0);
// console.log(x1);
// console.log(x2);
// console.log(x3);

// tu była cała masa takich kyu8 które sie robiło w 10sek na stronce

// Given an array of integers.
// Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
// 0 is neither positive nor negative.
// If the input is an empty array or is null, return an empty array.
// Example
// For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]

function countPositivesSumNegatives(input) {
  if (input === null || input === undefined || !input.length){
    return []
  } else {
    const pos = [];
    const neg = [];
    for (const i of input) {
      if (i > 0) {
        pos.push(i)
      } else if (i < 0) {
        neg.push(i)
      }
    }
    return [pos.length, neg.reduce((a, b) => a + b)]
  }
}

// const x = countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]);
// const x1 =countPositivesSumNegatives([]);
// console.log(x);
// console.log(x1);

// There was a test in your class and you passed it. Congratulations!
//
// But you're an ambitious person. You want to know if you're better than the average student in your class.
//
// You receive an array with your peers' test scores. Now calculate the average and compare your score!
//
// Return true if you're better, else false!
// Note:
//
// Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

function betterThanAverage(classPoints, yourPoints) {
  return ((classPoints.reduce((a, b) => a + b) + yourPoints)/(classPoints.length+1)) < yourPoints;
}

// const x1 = betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75);
// console.log(x1);
// const x2 = betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 9);
// console.log(x2);

// Write function bmi that calculates body mass index (bmi = weight / height2).
//
// if bmi <= 18.5 return "Underweight"
//
// if bmi <= 25.0 return "Normal"
//
// if bmi <= 30.0 return "Overweight"
//
// if bmi > 30 return "Obese"
function bmi(weight, height) {
  const bmi_ = weight / height**2;
  switch(true){
    case bmi_ <=18.5: return "Underweight";
    case bmi_ <= 25.0: return "Normal";
    case bmi_ <= 30.0: return "Overweight";
    default: return "Obese";
        }
}

// const x = bmi(80, 1.80);
// console.log(x);
// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
// // Note: input will never be an empty string
// to z ręki wpisałem i zadziałało:
// function fakeBin(x){
// const arr = []
// for (const i of x){
//   if (i <5){
//     arr.push(0);
//   }else{
//     arr.push(1);
//   }
// }return arr.join('')
// }



