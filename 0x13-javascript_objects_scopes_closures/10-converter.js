#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (x) {
    return x.toString(base);
  }

  return myConverter;
};
