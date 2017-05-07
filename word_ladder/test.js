const test = require('tape');
const { getNeighbours } = require('./generate_ladder.js');

console.log(getNeighbours);
test('get neighbours', (t) => {
    t.plan(2);

    t.ok(Array.isArray(getNeighbours('test'), 'returns an array'));

    t.deepEqual(
      getNeighbours('test', ['vest', 'vast', 'text']),
      ['vest', 'text'],
      'returns the right words');

});
