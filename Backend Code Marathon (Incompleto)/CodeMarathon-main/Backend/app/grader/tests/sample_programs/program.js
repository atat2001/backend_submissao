/*
Sample program for testing. Receives an integer as an input and prints that
input + 1.
*/


const readline = require('readline');


const rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});


rl.on("line", (input) => {
    number = parseInt(input) + 1;
    if (isNaN(number)) throw new Error("Input must be a number!");
    console.log(number)
    process.exit(0)
});
