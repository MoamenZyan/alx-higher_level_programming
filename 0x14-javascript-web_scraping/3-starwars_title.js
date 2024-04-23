#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
