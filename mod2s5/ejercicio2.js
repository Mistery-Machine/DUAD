/*Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista

/*filter*/

const numbers = [1, 2, 3, 4, 5, 6];

const newNumbers = numbers.filter((i) => {
  return i % 2 === 0;
});

console.log(newNumbers);
