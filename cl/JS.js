const car = {
    type: 'sedan',
    color: 'green',
    engine:'2.0'
}

console.log(car.type + ' ' + car.color + ' ' + car.engine)

let x = 2 + "dwa"
console.log(typeof(x))

// let howold = prompt('What is your age?');
// if (howold > 17){
//     alert("You are an adult, you can stay.");
// } else {
//     alert('You are an youngling, go back!');
// }

function factorial(number){
    let nums = 1
    for (let num = 2; num <=number; num++ ) {
        nums *= num
    }
    return nums
}
console.log(factorial(8))

function sum_(num1, num2){
    let nums = 0
    for (let num = num1; num <=num2; num++ ) {
        nums += num;
    }
    return nums;
}
console.log(sum_(8, 20))

const numbers = [4,4,1,2,5,40];
let avg = (numbers.reduce((a,b) => a + b)) / numbers.length;

console.log(avg)

function pointless_function() {
    const pointless = [];
    const nonesens = [];
    for (let i = 1; i <=10; i++) {
        pointless.push(Math.floor(Math.random() * 60) + 1);
    }
    for (let i of pointless) {
        if (i % 2 === 1) {
            nonesens.push(i +1);
        }
        else {
            nonesens.push(i);
        }
    }
    return nonesens
}
console.log(pointless_function())

