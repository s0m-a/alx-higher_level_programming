#!/usr/bin/node
const f = require('fs');
const path = process.argv[2];
const content = process.argv[3];

f.writeFile(path, content, err => {
  if (err) {
    console.error(err);
  }
});
