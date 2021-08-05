#!/usr/bin/node
const argv = process.argv;
const isNum = parseInt(argv[2]);
if (isNaN(isNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
