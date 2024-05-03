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

function summing(array){
   return array.reduce((a , b) => a +b);
   // let sum = 0
   // for (let i of array){
   //     sum += i;
   // }
   // return sum
}

console.log(summing([1,2,3,4,5,6]))

const more_pointless_nonesen = function(num1, num2, num3) {
    // const why_would_anyone_would_need_this_kind_of_bs = Math.max(num1, num2, num3);
    // return why_would_anyone_would_need_this_kind_of_bs
    return Math.max(num1, num2, num3)
}
console.log(more_pointless_nonesen(4, 99, 44))

function calculate_tip(amount, rating){
    if (rating === 'Bardzo dobra obsługa'){
        return amount*0.25
    } else if (rating === 'Dobra obsługa'){
        return amount*0.20
    }else if (rating === 'Średnia obsługa'){
        return amount*0.15
    }else if (rating === 'Zła obsługa'){
        return 0
    } else {
        return 'opis nieczytelny'
    }
}

console.log(calculate_tip(200, 'Dobra obsługa'))

function calculate_tip_proper(){
    const amount = parseFloat(prompt('Podaj kwotę na rachunku: '));
    const rating = prompt('Podaj opis jakości obsługi (Bardzo dobra obsługa, Dobra obsługa, Średnia obsługa, Zła obsługa): ');

    if (rating === 'Bardzo dobra obsługa'){
        alert('Napiwek do zapłaty: ' + (amount*0.25));
    } else if (rating === 'Dobra obsługa'){
        alert('Napiwek do zapłaty:' + (amount*0.20));
    }else if (rating === 'Średnia obsługa'){
        alert('Napiwek do zapłaty: ' + (amount*0.15));
    }else if (rating === 'Zła obsługa'){
        alert('Napiwek do zapłaty: 0');
    }
    else {
        alert('opis nieczytelny');
    }
}

console.log(calculate_tip_proper())