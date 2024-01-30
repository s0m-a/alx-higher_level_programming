#!/usr/bin/node
const request = require('request');

function getR (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function fetchAndPrintNames (urlFilm) {
  try {
    const fResponse = await getRequest(urlFilm);
    const fData = JSON.parse(fresponse.body);

    for (const cUrl of fData.characters) {
      const response = await getR(cUrl);
      const dat = JSON.parse(response.body);
      console.log(dat.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const urlF = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
gets(urlF);
