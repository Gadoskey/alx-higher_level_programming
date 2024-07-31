#!/usr/bin/node

// Importing the request Module
const request = require('request');

// Processing Command-Line Arguments. the first two arguments are stripped.
const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}


const url = args[0];

// Making a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  console.log('code: ' + response.statusCode)
});
