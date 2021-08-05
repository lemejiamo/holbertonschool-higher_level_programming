#!/usr/bin/node
function add(a, b) {
  return (a + b);
}

const argv = process.argv;
const numOne = parseInt(argv[2]);
const numTwo = parseInt(argv[3]);


console.log(add(numOne, numTwo));
