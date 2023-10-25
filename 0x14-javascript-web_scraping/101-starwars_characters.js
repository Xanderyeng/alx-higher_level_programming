#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a valid Movie ID as the first argument.');
  process.exit(1);
}

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);

      if (movieData.characters && movieData.characters.length > 0) {
        const charactersUrls = movieData.characters;

        charactersUrls.forEach((characterUrl, index) => {
          request(characterUrl, (charError, charResponse, charBody) => {
            if (!charError && charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } else {
              console.error('Error:', charError);
            }

            if (index === charactersUrls.length - 1) {
              // All characters printed, exit the script
              process.exit(0);
            }
          });
        });
      } else {
        console.log('No characters found for this movie.');
      }
    } else {
      console.error('Error:', response.statusCode, body);
    }
  }
});
