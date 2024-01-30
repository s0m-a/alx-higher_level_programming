#!/usr/bin/node
const f = require('fs');
const path = process.argv[2];

f.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
