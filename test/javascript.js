const R = require('ramda');
const myVarArrowFn = (these, those) => these - those;

const diff = (a, b) => a - b;

function sortAscending() {
  return diff;
}

R.sort(sortAscending, [45, 21, 8, 2, 86, 1, 5]);

function myFunction(param1, param2) {
  const str = 'string';
  const num = 1234567890;
  const bool = true || false;
  const newSymbol = Symbol();
  const obj = new Object();
  const arr = [];

  console.log(str, num, bool, newSymbol, obj, arr, param1, param2);
  return num > 0;
}

myFunction();

const num = 1234567890;
let myLet = num + 1;
myLet++;
const myConstArrowFn = something => something;

const somethingCool = myConstArrowFn;
const somethingElse = myVarArrowFn();

myVarArrowFn();

console.log(myLet, somethingCool, somethingElse);

R.sort(myVarArrowFn, [5, 4, 3, 2, 1]);
