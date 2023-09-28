#!/usr/bin/node

if (parseInt(process.argv[3])) {
  const myList = process.argv;
  const newList = myList.slice(2);
  newList.sort((a, b) => a - b);
  console.log(newList[newList.length - 2]);
} else {
  console.log('0');
}
