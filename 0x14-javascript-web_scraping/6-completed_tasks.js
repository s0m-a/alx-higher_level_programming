#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const dat = JSON.parse(body);
    const dic = {};
    dat.forEach((user) => {
      if (user.completed) {
        if (!dic[user.userId]) {
          dic[user.userId] = 1;
        } else {
          dic[user.userId] += 1;
        }
      }
    });
    console.log(dic);
  }
});
