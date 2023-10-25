#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
