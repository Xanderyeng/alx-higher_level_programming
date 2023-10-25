#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];
// const charUrl = 'https://swapi-api.hbtn.io/api/people/18/';
let numMovies = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const resultList = JSON.parse(body).results;
    resultList.forEach(function (charactersList) {
      charactersList.characters.forEach(function (character) {
        if (character.includes('18')) {
          numMovies++;
        }
      });
    });
    console.log(numMovies);
  }
});
