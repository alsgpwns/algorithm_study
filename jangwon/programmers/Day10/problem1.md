```js
function solution(numbers) {
    let set = new Set();
    let arr = numbers.split("").map((el)=>+el);
    let count = 0;
    
    const powerSet = (arr,str) => {
        if(arr.length) {
            for(let i=0; i< arr.length; i++) {
                let copyArr = [...arr];
                copyArr.splice(i,1);
                powerSet(copyArr,str + arr[i]);
            }
        }
        if(str > 0) set.add(+str);
    }
    
    powerSet(arr,"")
    
    let result = Array.from(set).sort((a,b)=>a-b);
    result = result.filter((el)=> el !==1 );
    
    // 소수 판별
    const isPrime = (number) => {
        if(number < 2) {
            return false;
        }
        let divider = 2;
        
        while(number > divider){
            if(number % divider === 0) return false
            divider++
        }
        return true
    }
    
    for(let i=0; i<result.length; i++) {
        if(isPrime(result[i])) {
            count++
        }
    }
    return count;
}
```



/*

    1) 문자열을 쪼갠후 나올수 있는 숫자를 모두 구한다. 
    2) 그 숫자가 소수 인지 판별한다. 
    3) 소수 판별은 자기자신과 1로만 나눠지기때문에 그 이전까지의 요소가 나머지가 0이면 안된다. 

*/