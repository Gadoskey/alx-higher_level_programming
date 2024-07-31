#!/usr/bin/node

// Importing the fs Module
const fs = require('fs');

// Defining the readFile fuction
const readFile = (filePath) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error: ${err}`);
      return;
    }
    console.log(data);
  });
};

// Processing Command-Line Arguments. the first two arguments are stripped.
const args = process.argv.slice(2);

// Checking Arguments And Calling The Function
if (args.length !== 1) {
  console.log('Usage: node script.js <file_path>');
} else {
  const filePath = args[0];
  readFile(filePath);
}
