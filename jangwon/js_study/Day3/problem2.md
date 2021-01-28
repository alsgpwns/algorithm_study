# 문제 3) 체육복 

https://programmers.co.kr/learn/courses/30/lessons/42862
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