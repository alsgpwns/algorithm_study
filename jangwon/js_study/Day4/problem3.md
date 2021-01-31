**풀이 1**

```js
function solution(n)
{
    var answer = 0;
    
    let arr = n.toString().split("").map((el)=> parseInt(el))
    for(let i=0; i< arr.length; i++){
        answer += arr[i]
    }
    return answer
}   
```
**풀이 2**

```js
function solution(n)
{
    return (n+"").toString("").split("").reduce((acc,val)=> acc + parseInt(val),0)
}
```