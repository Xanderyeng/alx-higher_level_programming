#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
file.writeFile(argv[2], argv[3], err => {
  if (err) {
    console.error(err);
  }
});
