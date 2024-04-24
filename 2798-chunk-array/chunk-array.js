/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let index = 0;
    let res = [];
    while (index < arr.length) {
        res.push(arr.slice(index, index+size));
        index += size;
    }        
    return res
};
