#!/usr/bin/node
const argv = process.argv;
const isNum = parseInt(argv[2]);
if (isNaN(isNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    let line = '';
    for (let j = 0; j < argv[2]; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
