# 문제 3) 약수의 합 

https://programmers.co.kr/learn/courses/30/lessons/12928


## 문제 풀이

**약수 구하기** 

자기보다 작은 수로 나뉘는 지 확인한다. 

자기와 나누어 나머지가 0이면 약수이다. 

1. 약수를 구한다.
2. 구한 약수를 모두 배열에 넣는다.
3. 배열을 순회하여 모두 더해 반환한다.
4. 마지막으로 1을 더해준다. 
    
```js
function solution(n) {
    let arr = [];
    let result = 0;

    for(let i =1; i <= n; i++ ){
        arr.push(i)
    }
    
    arr = arr.filter((el)=> n % el === 0)
    
    console.log(arr);
    
    for(let i = 0; i < arr.length; i++) {
        result += arr[i]
    }
    return result
}
``` 