```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hash = new Map();
    
    for(let i=0; i<nums.length; i++) {
        let complement = target - nums[i];
        if(hash.has(complement)) {
            return [i,hash.get(complement)];
        }
        hash.set(nums[i],i);
    }
};
```