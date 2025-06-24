function identifyingNumber(number, callbackOdd, callbackEven) {
  if (number % 2 === 0) {
    callbackEven();
  } else {
    callbackOdd();
  }
}

//Callbacks

function numberOdd() {
  console.log("Number entered is odd");
}

function numberEven() {
  console.log("Number entered is even");
}

//Prueba

identifyingNumber(4, numberOdd, numberEven);

identifyingNumber(7, numberOdd, numberEven);
