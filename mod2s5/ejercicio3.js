/*Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map*/

const celcius = [50, 30, 10, 25];

const newCelcius = celcius.map((i) => (i * 9) / 5 + 32);
console.log(newCelcius);
