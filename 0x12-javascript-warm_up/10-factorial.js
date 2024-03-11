#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log(1);
} else {
  let total = 1;
  for (let i = Number(process.argv[2]); i >= 1; i--) {
    total *= i;
  }
  console.log(total);
}
