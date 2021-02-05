```js
function solution(n, arr1, arr2) {
    let firstArr = arr1.map((el)=>el.toString(2)).map((el)=> +el);
    let secondArr = arr2.map((el)=>el.toString(2)).map((el)=>+el);
    
    let result = [];
    
    for(let i=0; i<firstArr.length; i++) {
        result.push(firstArr[i] + secondArr[i]);
    }
    
    result = result.map((el)=>(el+"").split(""))
    
     result.map((el)=> el.map((ele)=>{
        console.log(ele === "1" ? true :false)
    }))
}

/*
    문제풀이
    1) 2진수로 바꾸어준다.
    2) 각 요소를 더해준다. (요소를 숫자로 바꿔준다)
    3) 만약 2의 값이 나온다면 1로 바꿔준다. 
    4) 각 요소를 순회햐여 1이라면 #으로 바꿔준다.
    5) 만약 0이라면 공백으로 치환한다.
    6) 배열을 반환한다. 
    

*/
```