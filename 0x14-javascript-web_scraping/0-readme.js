#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
file.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
