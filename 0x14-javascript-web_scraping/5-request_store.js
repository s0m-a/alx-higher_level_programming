#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const fs = require('fs');
    const path = process.argv[3];

    fs.writeFile(path, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
