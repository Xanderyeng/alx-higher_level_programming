#!/usr/bin/node

const size = process.argv[2];
if (parseInt(size)) {
  for (let i = 1; i <= size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
