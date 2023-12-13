#!/usr/bin/node

const args = process.argv.slice(2);
const file = require('fs');
const A = file.readFileSync('./' + args[0]);
const B = file.readFileSync('./' + args[1]);
file.writeFileSync('./' + args[2], A + B);
