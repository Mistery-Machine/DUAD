/*Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los siguientes datos:*/

// Entrada
let total = 0;
const student = {
  name: "John Doe",
  grades: [
    { name: "math", grade: 80 },
    { name: "science", grade: 100 },
    { name: "history", grade: 60 },
    { name: "PE", grade: 90 },
    { name: "music", grade: 98 },
  ],
};

let highestGrade = student.grades[0].grade;
let lowestGrade = student.grades[0].grade;

let highestGradeName = student.grades[0].name;
let lowestGradeName = student.grades[0].name;

student.grades.forEach((i) => {
  total += i.grade;
  if (i.grade > highestGrade) {
    highestGrade = i.grade;
    highestGradeName = i.name;
  }
  if (i.grade < lowestGrade) {
    lowestGrade = i.grade;
    lowestGradeName = i.name;
  }
});
let gradeAvg = total / student.grades.length;
console.log(
  `average with ${gradeAvg}  highest grade is ${highestGradeName} with ${highestGrade} and lowest grade is ${lowestGradeName} with ${lowestGrade}`
);
