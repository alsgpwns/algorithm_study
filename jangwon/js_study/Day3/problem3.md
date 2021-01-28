# 문제 2) 약수의 합 

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



/*
    문제 이해 
    
    1. 학생들의 번호가 체격순 
    2. 바로 앞번호 또는 뒷번호의 학생에게만 체육복을 빌려 줄 수 있음
    3. 가장 많은 수를 찾는다. 
    
    전체 학생수 n 
    도난 당한 학생 번호가 담긴 배열 lost
    여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve

*/


/* 
    문제 풀이 

    1. 학생 default 배열을 생성한다. (정상적인 학생은 체육복을 가지고 있기 때문에 1로 모두 채워준다.)
    2. lost 인자를 이용하여 체육복이 없는 학생 배열을 만들어준다. 
    3. reserve를 통해 체육복이 없는 학생에게 보충해준다. 
*/
