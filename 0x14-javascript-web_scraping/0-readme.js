#!/usr/bin/node

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
});
