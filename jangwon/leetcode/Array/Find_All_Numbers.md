# Array

## Find All Numbers Disappeared in an Array

### https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/

**내 풀이**

```js
var findDisappearedNumbers = function(nums) {
    let arr = [];
    let result = [];
    let hash = new Map();
    
    // 배열에 삽입
    for(let i=1; i<=nums.length; i++) {
        arr.push(i);
    }
    
    // 해시 생성
    for(let el of nums){
        if(!hash.has(el)){
            hash.set(el,1);
        }else{
            hash.set(el,hash.get(el) + 1);
        }
    }
    
    for(let i=0; i<arr.length; i++) {
        if(!hash.has(arr[i])){
            result.push(arr[i]);
        }
    }
    
    return result;
};
```

```js
var findDisappearedNumbers = function(nums) {
    const set = new Set();
    
    for(let i=1; i<=nums.length; i++) {
        set.add(i);
    }
    
    for(let i=0; i<nums.length; i++) {
        if(set.has(nums[i])){
            set.delete(nums[i]);
        }
    }
    
    return [...set];
};
```