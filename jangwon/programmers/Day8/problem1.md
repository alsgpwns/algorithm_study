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