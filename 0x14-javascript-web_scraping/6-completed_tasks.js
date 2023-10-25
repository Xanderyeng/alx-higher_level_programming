#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const newDict = {};
request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    JSON.parse(body).forEach(function (data) {
      if (data.completed === true) {
        const userID = data.userId;
        if (!(userID in newDict)) {
          newDict[userID] = 0;
        }
        newDict[userID] += 1;
      }
    });
    console.log(newDict);
  }
});
