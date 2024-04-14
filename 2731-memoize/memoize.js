/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args); // Create a unique key based on function arguments
        if (cache.has(key)) {
            return cache.get(key); // If the result is already cached, return it
        } else {
            const result = fn(...args); // Call the original function
            cache.set(key, result); // Cache the result
            return result; // Return the result
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */