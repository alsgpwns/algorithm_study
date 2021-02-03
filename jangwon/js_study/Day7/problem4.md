**문제4**

### 정수 제곱근 판별 

https://programmers.co.kr/learn/courses/30/lessons/12934

**풀이1**

```js
function solution(n) {
    let number = Math.sqrt(n);
    
    if(!Number.isInteger(number)){
        return -1;
    }
    
    return Math.pow(number + 1, 2);
}
```

**풀이2**

```js
function solution(n) {
  return Number.isInteger(Math.sqrt(n)) ? Math.pow(Math.sqrt(n) + 1 ,2) : -1 
}
```

**다른 사람 풀이**

```js
function nextSqaure(n){
  switch(n % Math.sqrt(n)){
    case 0:
      return Math.pow(Math.sqrt(n) + 1, 2);
    default:
      return -1
  }
}
```

### 배운점 

* ```Math.sqrt()``` 메소드 : 루트를 씌워 해당 값을 반환
* ```Math.pow()``` 메소드 : 해당 값을 제곱
* ```Number.isInteger()``` 메소드 : 정수인지 판별 , 소수점인지 판별할때 유용