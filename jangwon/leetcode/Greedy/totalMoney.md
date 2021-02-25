# Greedy

## https://leetcode.com/problems/calculate-money-in-leetcode-bank/

* 내 풀이 

```js
var totalMoney = function(n) {
    let result = 0;
    let num = parseInt(n / 7);
    let module = n % 7
    let start = 1;
    
    while(num > 0){
        for(let i=start; i<start+7; i++){
            result += i;
        }
        start++
        num--
    }
    
    if(num === 0){
        for(let i=start; i<start+module; i++){
            result += i;
        }
        return result;
    }
};
```

* 다른 사람 풀이
  
```js
var totalMoney = function(n) {
  let result = 0;
  let counter = 0;
  while(true){
    for(let i=1;i<8;i++){
      if(n === 0) return result;
      result += i + counter;
      n--;
    }
    counter++;
  }
  return result;
};
```