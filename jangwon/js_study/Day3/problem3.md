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

## 코드

### 아직 다 풀지 못했습니다. 

```js
function solution(n, lost, reserve) {
    
    let student = Array(5).fill(1) ; 
    let result = 0;
    
    for(let i=0; i < lost.length; i++){
        student[lost[i] - 1] = student[lost[i] - 1] - 1
    }
    
    for(let i=0; i < reserve.length; i++) {
        if(student[reserve[i]] === 0 ) {
            student[reserve[i]]++
        }
        
        if(student[reserve[i] + 1] === 0){
            student[reserve[i] + 1]++
        }
    }
        
    for(let i= 0; i < student.length; i++) {   
        result += student[i]
    }
    return result
}
```