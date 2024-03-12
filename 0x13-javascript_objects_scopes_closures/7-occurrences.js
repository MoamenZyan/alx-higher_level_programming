#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let map = new Map();
  for (let i = 0; i < list.length; i++) {
    if (map.has(list[i])) {
      map.set(list[i], map.get(list[i]) + 1);
      continue;
    }
    map.set(list[i], 1);
  }

  return map.get(searchElement);
};
