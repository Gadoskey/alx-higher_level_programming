#!/usr/bin/node

// Importing the fs Module
const fs = require('fs');

// Processing Command-Line Arguments. the first two arguments are stripped.
const args = process.argv.slice(2);

const filePath = args[0];
const stringToWrite = args[1];

// Defining the writeFile fuction
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(`Error: ${err}`);
  }
});
