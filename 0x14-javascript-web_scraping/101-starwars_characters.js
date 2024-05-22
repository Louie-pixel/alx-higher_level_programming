#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  const characters = content.characters;
  // Array to hold all promises
  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  // Wait for all character promises to complete
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.log(error);
    });
});
