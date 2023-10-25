#!/usr/bin/node
const argv = process.argv;
const file = require('fs');
const request = require('request');
request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    file.writeFile(argv[3], body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
