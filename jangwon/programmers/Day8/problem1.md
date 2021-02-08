**문제1**

### 두 개 뽑아서 더하기 

https://programmers.co.kr/learn/courses/30/lessons/68644

```js
function solution(numbers) {
    let arr = numbers;
    let result = [];
    
    for(let i=0; i< arr.length; i++) {
        for(let j=i+1; j < arr.length; j++ ){
            result.push(arr[i] + arr[j]);
        }
    }
    
    result.sort((a,b)=>a-b);
    
    return result.filter((item,index)=> result.indexOf(item) === index);
        
}
```