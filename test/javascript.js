const R = require('ramda');

const truncate = R.when(
  R.propSatisfies(R.gt(R.__, 10), 'length'),
  R.pipe(R.take(10), R.append('...'), R.join(''))
);

truncate('12345');         // => '12345'
truncate('0123456789ABC'); // => '0123456789...'

const mapKeys = R.curry((fn, obj) => R.fromPairs(R.map(R.adjust(fn, 0), R.toPairs(obj))));

const myObj = mapKeys(R.toLower, { A: 1, B: 2, C: 3 });
// => { a: 1, b: 2, c: 3 }

R.fromPairs(myObj); // => [['a', 1], ['b', 2], ['c', 3]]

class Interpreter {

}
