#!/usr/bin/node

if (process.argv.length >= 4) {
  const arr = process.argv.slice(2);
  arr.sort((a, b) => b - a);
  console.log(Number(arr[1]));
} else {
  console.log(0);
}
