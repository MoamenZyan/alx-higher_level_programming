#!/usr/bin/node

function fact (a) {
  if (isNaN(Number(a))) {
    return 1;
  }
  if (a === 1) {
    return 1;
  }
  return a * fact(a - 1);
}

console.log(fact(process.argv[2]));
