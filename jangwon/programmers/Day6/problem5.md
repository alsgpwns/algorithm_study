**문제5**

### x만큼 간격이 있는 n개의 숫자

https://programmers.co.kr/learn/courses/30/lessons/12954

```js
function solution(x, n) {
    let arr = [];
    
    for(let i=1; i <= n; i++) {
        arr.push(i * x)
    }
    return arr;
}
```

```js
function solution(x, n) {
 return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
```