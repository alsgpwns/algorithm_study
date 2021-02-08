**문제4**

### 비밀지도

https://programmers.co.kr/learn/courses/30/lessons/17681

**문제풀이 -> 비트연산자**

1) 2진수로 바꾸어준다.
2) 비트연산을 사용하여 이진수를 바꿔준다. (요소를 숫자로 바꿔준다)
3) 바꿔준 비트연산 앞에 0을 넣어준다. 
4) 뒤로 배열의 col만큼 얕은 복사를 진행한다.
5) replace함수를 사용하여 원하는 값으로 치환한다. 

```js
function solution(n, arr1, arr2) {
    let arr =  arr1.map((el,i)=> ('0'.repeat(n) + (el | arr2[i]).toString(2)).slice(-n));
    
    return arr.map((el)=> el.replace(/0/g , " ").replace(/1/g,"#"));
}
```

### 레퍼런스
* https://velog.io/@jakeseo_me/2019-04-30-1604-%EC%9E%91%EC%84%B1%EB%90%A8-7qjv3gv9ad
  
*  https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/