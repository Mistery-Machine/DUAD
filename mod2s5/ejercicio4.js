/*Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split.*/

const example = "This is a string!";
const secondList = [];
let word = "";

for (let i of example) {
  if (i != " ") word += i;
  else secondList.push(word), (word = "");
}
if (word) {
  secondList.push(word);
}
console.log(secondList);
