#!/usr/bin/node
exports.esrever = function (list) {
  const reverlist = [];
  const size = list.length;
  let j = 0;
  for (let i = (size - 1); i >= 0; i--, j++) {
    reverlist[j] = list[i];
  }
  return reverlist;
};
