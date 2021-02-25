# String

## 문제 : isPrefixOfWord

### https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/submissions/

<img width="532" alt="스크린샷 2021-02-25 오후 4 37 20" src="https://user-images.githubusercontent.com/33803975/109119311-d99a7200-7787-11eb-8e58-cbfb2d02bf28.png">


* 내 풀이 

```js
var isPrefixOfWord = function(sentence, searchWord) {
    let arr = sentence.split(" ");
    let idx = [];
    let result = 0;
    
    for(let i =0; i<arr.length; i++){
        let count = 0;
        for(let j=0; j<searchWord.length; j++){
            if(arr[i][0] === searchWord[0]){
                if(arr[i][j] === searchWord[j]){
                    count++;
                }
            }
        }
        if(count === searchWord.length){
            idx.push(i);
            result = count;
        }
    }

    if(result < searchWord.length){
        return -1;
    }
    
    if(result >= searchWord.length){
        return Math.min(...idx) + 1;
    }
};
```