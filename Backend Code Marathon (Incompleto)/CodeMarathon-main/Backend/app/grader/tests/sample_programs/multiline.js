/*
Sample program for testing. Receiving and outputting multiple lines. It
receives 2 numbers, prints their adition and their multiplication.
*/
var readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

var inputs = [];

rl.on("line", (input) => {
  const number = parseInt(input);
  if(isNaN(number)) throw new Error("Input must be a number!")
  inputs.push(number);
  if(inputs.length == 2){
    console.log(inputs[0] + inputs[1])
    console.log(inputs[0] * inputs[1])
    process.exit(0);
  }
});
