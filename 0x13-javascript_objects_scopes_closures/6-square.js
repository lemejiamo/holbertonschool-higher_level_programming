#!/usr/bin/node
const squareold = require('./5-square');

class Square extends squareold {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line = `${line}${c}`;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
