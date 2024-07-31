#!/usr/bin/node

// Importing the request Module
const request = require('request');

// Processing Command-Line Arguments. the first two arguments are stripped.
const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = args[0];
if (args.length !== 1) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}


// Making a GET request to the specified URL
request(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsObject = JSON.parse(body);
    console.log(jsObject.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
