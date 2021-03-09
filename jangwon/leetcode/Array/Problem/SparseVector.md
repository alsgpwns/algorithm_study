# Array , Two Pointer , Hash Table

## 1570. Dot Product of Two Sparse Vectors

* 풀이 

```js

/**
 * @param {number[]} nums
 * @return {SparseVector}
 */
var SparseVector = function(nums) {
    this.hash = new Map();
    nums.map((el,idx)=>{
        if(el !==0) {
            this.hash.set(idx,el);
        }
    })
};

// Return the dotProduct of two sparse vectors
/**
 * @param {SparseVector} vec
 * @return {number}
 */
SparseVector.prototype.dotProduct = function(vec) {
    let result = 0;
    for(const el of this.hash){
        if(vec.hash.has(el[0])) {
            result += vec.hash.get(el[0]) * el[1];
        }
    }
    return result;
};

```

* 레퍼런스 풀이 

```js
/**
 * @param {number[]} nums
 * @return {SparseVector}
 */
var SparseVector = function(nums) {
    this.vector = nums;
};

// Return the dotProduct of two sparse vectors
/**
 * @param {SparseVector} vec
 * @return {number}
 */
SparseVector.prototype.dotProduct = function(vec) {
    return this.vector.reduce((acc,val,idx)=>{
        return acc = acc + val * vec.vector[idx];
    },0)
};
```