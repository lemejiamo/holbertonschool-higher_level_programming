#!/usr/bin/node
const Square_old = require('./5-square');

class Square extends Square_old {
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
