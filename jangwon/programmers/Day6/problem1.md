
**문제1**

### 정수 내림차순으로 배치하기

https://programmers.co.kr/learn/courses/30/lessons/12933

```js
function solution(n) {
   return +(n + "").split("").sort((a,b)=> b - a).join("")
}
```