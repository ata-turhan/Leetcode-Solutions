/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const map = new Map();
    for (let e of this) {
        let key = fn(e);
        if (!map.has(key))
            map.set(key, []);
        map.get(key).push(e)    
    }
    const array = {}
    for (let [key, val] of map)
        array[key] = val;
    return array;
    
    
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */