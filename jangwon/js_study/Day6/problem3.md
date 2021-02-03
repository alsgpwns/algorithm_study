**문제3**

### 핸드폰 번호 가리기

https://programmers.co.kr/learn/courses/30/lessons/12948

```js
function solution(phone_number) {
    let arr = phone_number.split("");
    
    for(let i =0; i< arr.length -4; i++) {
        arr[i] = "*"
    }
    return arr.join("");
}
```
      
            
            