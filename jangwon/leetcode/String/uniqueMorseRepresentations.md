# String

## 804. Unique Morse Code Words

* https://leetcode.com/problems/unique-morse-code-words/

* 내 풀이 

```js 
var uniqueMorseRepresentations = function(words) {
    let strArr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    let arr = [];
    
    for(let i=0; i<words.length; i++){
        let result = "";
        words[i].split("").map((el)=>{
            result += strArr[el.charCodeAt() - 97]
        })
        arr.push(result);
    }
    
    return [...new Set(arr)].length;
};
```

```js
var uniqueMorseRepresentations = function(words) {
    var morse = [".-","-...","-.-.","-..",".","..-.",
                  "--.","....","..",".---",
                  "-.-",".-..","--","-.","---",".--.",
                  "--.-",".-.","...","-","..-","...-",
                  ".--","-..-","-.--","--.."];
    
    var transformations = new Set();
    
    for (let word of words) {        
        var trans = "";
        for (let letter of word) {
            var index = letter.charCodeAt(0) - 97;
            trans += morse[index];
        }
        
        transformations.add(trans);   
    }
    
    return transformations.size;
};
```

### 배운 점

* `for of`문의 중첩
* `size` 함수 