### 하샤드 수

**문제1** 

https://programmers.co.kr/learn/courses/30/lessons/12947

**문제 풀이**

1. 주어진 x값을 문자열로 변환 ```toString()``` 대신 ``` + "" ``` 로 문자열을 처리함
2. 배열 메소드를 사용하기 위해 ```split()```로 배열로 변경해줌 
3. 여러개의 요소를 더해 한개의 값을 도출하기 위해 ```reduce()``` 를 사용
4. 각 요소들을 숫자로 만들어 더 해주어야하기 때문에 각 요소를 숫자로 바꿔준다. ```Number()``` , ```ParseInt()```, ```+``` 중에 ```+```를 사용하여 문자열을 숫자로 형 변환
5. 마지막 조건문으로 처리

```js
function solution(x) {
    let number = (x + "").split("").reduce((acc,val) => +((+acc) + (+val)));

    if(x % number === 0){
        return true;
    }
    return false;
}
```