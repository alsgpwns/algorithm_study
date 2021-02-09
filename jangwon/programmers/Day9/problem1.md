## 스택/큐

### 문제 1

**기능개발**

https://programmers.co.kr/learn/courses/30/lessons/42586**

**문제풀이** 

```js
function solution(progresses, speeds) {
    let result =[];
    
    while(speeds.length > 0) {
        for(let i=0; i< speeds.length; i++) {            
            if(progresses[i] < 100) {
                progresses[i] += speeds[i];
            }
        }
        let count = 0;
        while(progresses[0] >= 100) {
            progresses.shift();
            speeds.shift();
            count++
        }
        
        if(count > 0)  {
            result.push(count);
        }
    }
    
    return result;
}
```

