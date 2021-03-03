# String

## 1768. Merge Strings Alternately

* https://leetcode.com/problems/merge-strings-alternately/

<p align="center">
    <img width="532" alt="스크린샷 2021-02-25 오후 4 37 20" src="https://user-images.githubusercontent.com/33803975/109140870-69e4b100-77a0-11eb-995e-c059ceedb792.png">
</p>

* 내 문제 풀이

```js
var mergeAlternately = function(word1, word2) {
    let result = ""
    
    // case1
    if(word1.length === word2.length){
        for(let i=0; i<word1.length; i++){
            result += word1[i] + word2[i];
        }
    }
    
    // case2
    if(word1.length < word2.length){
        for(let i=0; i<word1.length; i++){
            result += word1[i] + word2[i];
        }
        for(let i=word1.length; i<word2.length; i++){
            result += word2[i];
        }
    }
    
    // case3
    if(word1.length > word2.length){
        for(let i=0; i<word2.length; i++){
            result += word1[i] + word2[i];
        }
        for(let i=word2.length; i<word1.length; i++){
            result += word1[i];
        }
    }
    
    return result;
};
```


