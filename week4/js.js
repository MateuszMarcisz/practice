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

x1 = lottery('hPrBKWDH8yc6Lt5NQZWQ');
console.log(x1);
x2 = lottery('555');
console.log(x2);
x3 = lottery("ynMAisVpHEqpqHBqTrwH");
console.log(x3);