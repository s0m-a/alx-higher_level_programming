#!/usr/bin/node
const request = require('request');
let count = 0;
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const dat = JSON.parse(body);
    dat.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(18)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
