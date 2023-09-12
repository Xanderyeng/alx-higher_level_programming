#!/usr/bin/node
const list = require('./100-data').list;
const procesList = list.map((x, index) => x * index);
console.log(list);
console.log(procesList);
