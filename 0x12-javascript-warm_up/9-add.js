#!/usr/bin/node

function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    console.log('NaN');
  } else {
    const total = Number(a) + Number(b);
    console.log(total);
  }
}

add(process.argv[2], process.argv[3]);
