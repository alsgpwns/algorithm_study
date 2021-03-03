# String

## 문제 : isPrefixOfWord

**https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/submissions/**

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

* 레퍼런스를 본 후 적용 풀이

```js
var isPrefixOfWord = function(sentence, searchWord) {
    let word = sentence.split(" ");
    let idx = word.findIndex((el) => el.startsWith(searchWord));
    if(idx >= 0){
        return idx + 1;
    }
    return idx;
};
```


**다른 사람 풀이** 

* 풀이 1
```js
const isPrefixOfWord = (sentence, searchWord) => {
  sentence += ' ';
  for (let i = 0, j = 1, word = ''; i < sentence.length; ++i) {
    if (sentence[i] !== ' ') { word += sentence[i]; continue; }
    if (word.startsWith(searchWord)) return j;
    ++j;
    word = '';
  }
  return -1;
};
```


```js
const isPrefixOfWord = (sentence, searchWord) => {
  const words = sentence.split(' ');
  for (let i = 0; i < words.length; ++i) {
    if (words[i].startsWith(searchWord)) return i + 1;
  }
  return -1;
};
```

### 배운점 

* `StartsWith()`

> startsWith() 메소드는 어떤 문자열이 특정 문자로 시작하는지 확인하여 결과를 true 혹은 false로 반환합니다.

* `findIndex()`

> findIndex() 메서드는 주어진 판별 함수를 만족하는 배열의 첫 번째 요소에 대한 인덱스를 반환합니다. 만족하는 요소가 없으면 -1을 반환합니다.

### Reference

* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith

* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex