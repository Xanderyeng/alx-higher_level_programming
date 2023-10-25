#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const filmID = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmID;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const resultList = JSON.parse(body).characters;
    resultList.forEach(function (character) {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
