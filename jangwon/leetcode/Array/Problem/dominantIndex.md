# Array

## https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/

* 풀이 
1) 가장 큰 요소를 구한다.
2) 가장 큰 요소를 제외한다.
3) 나머지 요소에 2를 곱해 가장 큰 요소와 비교한다.
4) 나머지 조건에 따른다. 


```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let max = Math.max(...nums);
    let idx = 0;
    let arr = nums;
    nums.map((el,i)=>{
        if(el === max){
            idx = i;
        }
    })
    
    nums = nums.filter((el)=> el !== max);
    
    for(let num of nums) {
        let twice = num * 2;
        if(twice > max){
            return -1;
        }
    }
    return idx;
};
```

> 시간복잡도 O(N), 공간복잡도 O(1)

* 풀이 2

```js
var dominantIndex = function(nums) {
    let first = Math.max(...nums);
    let idx = 0;
    nums.map((el,i)=>{
        if(el === first){
            idx = i;
            nums.splice(idx,1);
        }
    });
    let second = Math.max(...nums);
    
    if(second * 2 > first){
        return -1;
    }
    return idx;
};
```