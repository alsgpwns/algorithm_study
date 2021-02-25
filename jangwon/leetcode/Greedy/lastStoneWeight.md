# Greedy

## https://leetcode.com/problems/last-stone-weight/

* 내 풀이 

```js
var lastStoneWeight = function(stones) {
    stones.sort((a,b)=>a-b);
    
    while(stones.length > 1){
        let x , y = 0;
        y = stones[stones.length -1];
        x = stones[stones.length -2];
        
        if(x === y){
            let removeY = stones.indexOf(y);
            let removeX = stones.indexOf(x);
            stones.splice(removeY,1);
            stones.splice(removeX,1);
            stones.sort((a,b)=>a-b);
        }else{
            for(let i=0; i<stones.length; i++){
                if(stones[i] === y){
                    stones[i] = y - x;
                }
            }
            let removeX = stones.indexOf(x);
            stones.splice(removeX,1);
            stones.sort((a,b)=>a-b);
        }
    }
    
    if(stones.length === 1) {
        return stones[0];
    }
    
    if(!stones.length){
        return [];
    }
    
};
```

* 다른 사람 풀이

```js
var lastStoneWeight = function(stones) {
    while (stones.length > 1) {
        let max1 = Math.max(...stones);
        stones.splice(stones.indexOf(max1),1);
        let max2 = Math.max(...stones);
        stones.splice(stones.indexOf(max2),1);
        if (max1 !== max2) stones.push(Math.abs(max1-max2));       
    }
    return stones[0] || 0;
};
```