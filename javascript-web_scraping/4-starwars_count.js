#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach((film) => {
      const hasWedge = film.characters.some((characterUrl) => {
        return characterUrl.includes('/people/18/');
      });
      if (hasWedge) {
        count++;
      }
    });

    console.log(count);
  }
});
