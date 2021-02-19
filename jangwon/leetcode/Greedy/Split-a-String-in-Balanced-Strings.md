# Greedy(그리디)

## 1221. Split a String in Balanced Strings

### https://leetcode.com/problems/split-a-string-in-balanced-strings/


<p align="center">
  <img src= "https://user-images.githubusercontent.com/33803975/108325503-79964f80-720c-11eb-8b84-4b0fc74ca70b.png"/>
</p>

* 내 풀이

```js
var balancedStringSplit = function(s) {
    let count = 0;
    let result = 0;
    let arr = s.split("");
    
    arr.map((el)=>{
        if(count === 0) result++
        
        if(el === "R"){
            count++
        }else {
            count--
        }
    })
    
    return result;
};
```


```js
var balancedStringSplit = function(s) {
    let count = 0;
    let result = 0;
    
    for(let el of s) {
        if(count === 0) result++;
        if(el === "R") {
            count++;
        }else {
            count--;
        }
    }
    
    return result;
};
```

```js
var balancedStringSplit = function(s) {
    let count = 0;
    let result = 0;
    for(let i=0; i<s.length; i++) {
        if(count === 0) result++
        s[i] === "R" ? count++ : count--;
    }
    return result;
};
```