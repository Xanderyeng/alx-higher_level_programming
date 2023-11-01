const $ = window.$;
const url= 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (response) {
    for (const film of response.results) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
     }
});
