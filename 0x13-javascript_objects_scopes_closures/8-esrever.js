#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  const temp = list.length - 1;
  for (let a = temp; a >= 0; a--) {
    reversedList.push(list[a]);
  }
  return (reversedList);
};
