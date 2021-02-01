## 문제 5

**평균 구하기**

https://programmers.co.kr/learn/courses/30/lessons/12944

```js
function solution(arr) {
    return arr.reduce((acc,val) => (acc + val)) / arr.length
}
```

```js
function solution(arr) {
    let result = 0; 
    
    for(let i=0; i < arr.length; i++) {
        result += arr[i]
    }
    
    return result / arr.length
}
```