**문제5**

### 최대공약수와 최소공배수

https://programmers.co.kr/learn/courses/30/lessons/12940?language=javascript


```js
function solution(a, b) {
    var answer = [];
    var minNum = Math.min(a, b);
    var maxNum = Math.max(a, b);
    answer.push(gcd(minNum, maxNum))
    answer.push(lcm(minNum, maxNum))
    return answer;
}
// 최대공약수
function gcd(minNum, maxNum){
  return (minNum % maxNum) === 0 ? maxNum : gcd(maxNum, minNum % maxNum);
}
// 최소공배수
function lcm(minNum, maxNum){
  return minNum * maxNum / gcd(minNum, maxNum);
}
```