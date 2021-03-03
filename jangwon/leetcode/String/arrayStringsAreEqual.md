# String

## 1662. Check If Two String Arrays are Equivalent

* https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

* 내 풀이

```js
var arrayStringsAreEqual = function(word1, word2) {
    let str1 = word1.reduce((acc,val)=>acc+val,"");
    let str2 = word2.reduce((acc,val)=>acc+val,"");
    return str1 === str2 ? true : false;
};
```

* 다른 사람 풀이

```js
var arrayStringsAreEqual = function(word1, word2) {
    return word1.join('') === word2.join('')
};
```