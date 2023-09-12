#!/usr/bin/node

const myString = 'C is fun';
const x = process.argv[2];
if (parseInt(x)) {
  for (let i = 1; i <= x; i++) {
    console.log(myString);
  }
} else {
  console.log('Missing number of occurrences');
}
