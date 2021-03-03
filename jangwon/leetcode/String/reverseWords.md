# String

## 557. Reverse Words in a String III

* https://leetcode.com/problems/reverse-words-in-a-string-iii/
  
```js
var reverseWords = function(s) {
    return s.split(" ").map((el)=>el.split("").reverse().join("")).join(" ");
};
```

```js
var reverseWords = function(s) {
    let str = s.split(" ");
    let result = [];
    
    for(let el of str){
        result.push(el.split("").reverse().join(""));
    }
    
    return result.join(" ");
};
```
