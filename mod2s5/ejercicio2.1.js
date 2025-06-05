//Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista

//for

const numbers = [1, 2, 3, 4, 5, 6];
let evenNumbers = [];

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) evenNumbers.push(numbers[i]);
}
console.log(evenNumbers);
