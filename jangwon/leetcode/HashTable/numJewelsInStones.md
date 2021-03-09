# Hash

## 771. Jewels and Stones

### https://leetcode.com/problems/jewels-and-stones/

* 풀이

```js
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    let j = jewels.split("");
    let s = stones.split("");
    let count = 0;
    let hash = new Map();
    for(const el of s){
        if(!hash.has(el)){
            hash.set(el,1);
        }else{
            hash.set(el,hash.get(el)+1);
        }
    }
    for(const el of j){
        if(hash.has(el)){
            count += hash.get(el);
        }
    }
    return count;
};
```

```js
const numJewelsInStones = function(jewels, stones) {
    const jewel = new Set(jewels);
    return stones.split('').reduce((result,val)=>(jewel.has(val) ? result++ : result),0);
};
```