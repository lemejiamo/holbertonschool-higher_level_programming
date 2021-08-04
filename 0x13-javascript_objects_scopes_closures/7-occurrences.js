#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {

  let match = searchElement;
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    if (match === list[i]) {
        count += 1;
    }
  }
  return count;
}