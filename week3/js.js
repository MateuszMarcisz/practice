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

result = isIsogram('Dermatoglyphics');
console.log(result);
result1 = isIsogram('aba');
console.log(result1);
result2 = isIsogram('moOse');
console.log(result2);
