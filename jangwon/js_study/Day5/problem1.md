## 문제 1 

**완주 하지 못한 선수**

https://programmers.co.kr/learn/courses/30/lessons/42576


```js
function solution(participant, completion) {
    participant.sort();
    completion.sort();
    
    for(let i=0; i<participant.length; i++) {
        if(participant[i] !== completion[i]){
           return participant[i]
        }
    }
}
```