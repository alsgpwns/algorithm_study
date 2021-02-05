# 문자열 내마음대로 정렬하기 

https://programmers.co.kr/learn/courses/30/lessons/12915

**풀이**

```js

function solution(strings, n) {
  return strings.sort((a, b) => a[n] == b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]));
 }

 ```

## 배운 점들 

 
### 오름차순 정렬

```js
function solution(strings, n) {
  strings.sort((a, b) => a - b )
}
```

### 문자열의 n번째 글자를 기준으로 오름차순 정렬 

```js
function solution(strings, n) {
  strings.sort((a, b) => a[n] - b[n])
}
```

### n번째 글자가 같은 경우, 사전순으로 정렬 

자바 내장메소드 ```localCompare()```

```js
function solution(strings, n) {
  strings.sort(function(a, b) {
  	if(a[n] == b[n]) {
    	a.localeCompare(b)
    } else {
    	a[n].localeCompare(b[n])
    }
  })
}
```