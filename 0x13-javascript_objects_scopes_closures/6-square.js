#!/usr/bin/node

const SquareE = require('./5-square');

class Square extends SquareE {
  charPrint (c) {
    let char;
    if (c !== undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      let chars = '';
      for (let j = 0; j < this.width; j++) {
        chars += char;
      }
      console.log(chars);
    }
  }
}

module.exports = Square;
