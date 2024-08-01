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
//const id = 18;
//const fullUrl = `${url}${id}`;
// Making a GET request to the specified URL
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsObject = JSON.parse(body);
    let charWedgeUrl = jsObject.results[6][8];
    console.log(charWedgeUrl);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
/*request(fetchWedgeUrl, function (err, response, body){
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const charObj = JSON.parse(body);
    console.log(charObj.films.length);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});*/
