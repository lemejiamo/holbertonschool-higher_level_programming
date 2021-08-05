#!/usr/bin/node
const dictionary = require('./101-data').dict;
const newDict = {};

for (const key in dictionary) {
  if (!newDict[dictionary[key]]) {
    newDict[dictionary[key]] = [];
  }
  newDict[dictionary[key]].push(key);
}
console.log(newDict);
