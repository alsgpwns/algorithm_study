# 문자열 내림차순으로 배치하기 
https://programmers.co.kr/learn/courses/30/lessons/12917


**풀이**

1. 문자열을 배열로 만들어주고 sort를 통해 문자열을 배치한다.

2. 기본적으로 오름차순이기 때문에 ```reverse()``` 자바스크립트 내장메소드를 사용하여 내림차순 바꾼다.

3. 마지막으로 배열을 다시 문자열로 합쳐준다. 

```js
function solution(s) {
  var answer = s.split("").sort().reverse().join("");
  return answer;
}
```
