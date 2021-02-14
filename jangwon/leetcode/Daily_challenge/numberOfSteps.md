### 재귀 

```js
var numberOfSteps  = function(num) {
    
    const recur = (number) => {
        let count = 0;
        
        while(number > 0){
            count++
            number % 2 === 0 ? number = number/2  : number = number -1
            recur(number);
        }
        return count
    }
    
    return recur(num);
};
```

### 반복문

```js
var numberOfSteps  = function(num) {
    let count = 0;
    while(num > 0) {
        count++
        num % 2 === 0 ? num = num / 2 : num = num -1
    }
    
    return count;
};
```