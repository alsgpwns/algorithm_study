## 문제 3

**이상한 문자 만들기**

https://programmers.co.kr/learn/courses/30/lessons/12930

**풀이1**

```js
function solution(s) {
    let arr = s.split(" ");
    
    for(let i=0; i < arr.length; i++) {
        arr[i] = arr[i].split("");
        arr[i].forEach((el,i,arr) => {
            i % 2=== 0 ? arr[i] = arr[i].toUpperCase() : arr[i] = arr[i].toLowerCase();
        })
        arr[i] = arr[i].join("");
    }
    return arr.join(" ");
}
```

**풀이2**

```js
function solution(s) {
    return s.split(" ").map((el) => el.split("").map((j,i) => i % 2 === 0 ? j.toUpperCase() : j.toLowerCase()).join("")).join(" ")
}
```