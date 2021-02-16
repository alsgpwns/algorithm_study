# leetCode

**Array 문제 169**

## [169. Majority Element]:[**https://leetcode.com/problems/majority-element/**]

### HashMap 풀이

```js
var majorityElement = function(nums) {
    const hash = {};
    
    for(let el of nums) {
        if(!hash[el]){
            hash[el] = 0;
        }
        hash[el]++
        
        if(hash[el] > nums.length / 2) {
            return el
        }
    }
};
```

### HashMap Es6 풀이 

```js
var majorityElement = function(nums) {
    if(nums.length === 0) {
        return nums[0];
    }
    
    const hash = new Map();
    
    let half = (nums.length / 2);
    
    for(let num of nums){
        if(!hash.has(num)){
            hash.set(num,1);
        }else{
            hash.set(num,hash.get(num) + 1);
        }
        
        if(hash.get(num) > half){
            return num;
        }
    }
};
```