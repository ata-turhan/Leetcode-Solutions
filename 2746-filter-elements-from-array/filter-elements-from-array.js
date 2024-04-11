/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    res = []
    for (let i = 0; i < arr.length; i++)
        if (fn(arr[i], i))
            res.push(arr[i])
    return res
};