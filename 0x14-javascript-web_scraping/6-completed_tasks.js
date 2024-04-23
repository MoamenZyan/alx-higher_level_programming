#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], { json: true }, (err, res, body) => {
  if (err) {
        console.log(err);
        return;
  }

  const tasksCompleted = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
