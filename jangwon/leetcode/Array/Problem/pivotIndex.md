# Array

## https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

* 풀이 

1. 피봇의 왼쪽과 오른쪽을 나눈다. 

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let pivot = 0;
    
    while(pivot < nums.length){
        let lSum = 0;
        let rSum = 0;
        
        for(let i=0; i <= pivot; i++){
            lSum += nums[i];
        }        
        for(let i=pivot; i<nums.length; i++){
            rSum += nums[i];
        }
        if(lSum === rSum){
            return pivot;
        }
        pivot++;
    }
    return -1;
};
```

### solution

* 풀이 

1. 왼쪽의 합을 알고 있으면 오른쪽의 합을 알 수있다.
2. 왼쪽의 합과 오른쪽의 합을 비교하여 pivot을 구한다.
3. 시간복잡도 O(N)와 공간 복잡도 O(1)로 준수한 풀이로 풀 수 있다.

```js
var pivotIndex = function(nums) {
    const sum = nums.reduce((r, n) => r + n);
    
    let lSum = 0;
    for(let i=0; i< nums.length; i++) {
        const rSum = sum - lSum - nums[i];
        if(lSum === rSum){
            return i;
        }
        lSum += nums[i];
    }
    return -1;
};
```