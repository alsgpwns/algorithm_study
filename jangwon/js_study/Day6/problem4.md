**문제4**

### 콜라츠 추측

https://programmers.co.kr/learn/courses/30/lessons/12943

**풀이1**

```js
function solution(num) {
    const collatzRecursive = (input , count) => {
        if(count > 500) return -1;
        if(input === 1) return count;
        if(input % 2 === 0 ) return  collatzRecursive(input / 2, count +1);
        else return collatzRecursive(input * 3 + 1, count +1)
    }
    
    return collatzRecursive(num ,0);
}
```

**풀이2**

```js
function solution(num) {
    let count = 0; 
    
    while(num < 500) {
        if(num === 1){
            return count;
        }
        count++
        num = num % 2 === 0 ? num / 2 : num * 3 + 1
    }
    
    return -1
}
```