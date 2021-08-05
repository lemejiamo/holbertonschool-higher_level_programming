#!/usr/bin/node
const sum = function add(a, b) {
	return a + b;
}

const argv = process.argv;
let numOne = parseInt(argv[2]);
let numTwo = parseInt(argv[3]);

if (isNaN(numOne) || isNaN(numTwo)) {
	return;
}

console.log(sum(numOne, numTwo));
