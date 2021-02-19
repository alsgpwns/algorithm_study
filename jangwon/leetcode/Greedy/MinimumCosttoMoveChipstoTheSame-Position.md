# Greedy

## 1217. Minimum Cost to Move Chips to The Same Position

### https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

* 내 문제 풀이

```js
var minCostToMoveChips = function(position) {
    let oddCount = 0;
    let evenCount = 0;
    position.map((el)=>{
        if(el % 2 === 0) {
         evenCount++   
        }else{
            oddCount++
        }
    })
    
    if(oddCount >= evenCount) {
        return evenCount;
    }
    
    if(evenCount > oddCount) {
        return oddCount;
    }
};
```

```js
var minCostToMoveChips = function(position) {
    let oddCount = 0;
    let evenCount = 0;
    position.map((el)=> el % 2 === 0 ? evenCount++ : oddCount++);
    return Math.min(evenCount,oddCount);
};
```