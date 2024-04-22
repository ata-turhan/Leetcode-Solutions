/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        if (functions.length === 0) {
            resolve([]); // Resolve with an empty array if no functions are provided
        } else {
            const res = new Array(functions.length);
            let count = 0; // Counter to track resolved promises

            functions.forEach((func, idx) => {
                func().then(
                    result => {
                        res[idx] = result;
                        count++; // Increment counter when promise resolves
                        if (count === functions.length) 
                            resolve(res); // Resolve with results array when all promises are resolved
                    }
                ).catch(
                    err => reject(err) // Reject if any promise rejects
                );
            });
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */