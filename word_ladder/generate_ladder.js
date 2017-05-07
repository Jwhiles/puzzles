
// Str -> Int -> Char -> Str
const  setCharAt = (str,index,chr) => {
    return str.substr(0,index) + chr + str.substr(index+1);
}


// Str -> [Str] -> [Str]
const getNeighbours = (word, dictionary = []) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

  return word.split('')
    .reduce((acc, x, i) => acc.concat(
        alphabet.map(x => setCharAt(word, i, x))), [])
    .filter(word => dictionary.includes(word))
}
// 
// const crawlTree = (startWord, target, maxDepth) => {
//   let wordGroups = {}
//
// }

module.exports = {
    getNeighbours
}
