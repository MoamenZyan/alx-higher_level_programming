#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const char = 'X';
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let output = '';
    for (let j = 0; j < Number(process.argv[2]); j++) {
      output += char;
    }
    console.log(output);
  }
}
