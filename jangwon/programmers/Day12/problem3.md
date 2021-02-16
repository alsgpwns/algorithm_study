# 해시

## 위장 

https://programmers.co.kr/learn/courses/30/lessons/42578

### Two way hash 풀이 

```js
function solution(clothes) {
    let hash = {};
    let result = 1;
    
    for(let cloth of clothes) {
        if(!hash[cloth[1]]){
            hash[cloth[1]] = 1;
        }else{
            hash[cloth[1]]++
        }
    }
    
    for(let el in hash){
        result *= hash[el] + 1;
    }
    
    return result -1;
}
```

### ES6 Map을 이용한 풀이 

```js
function solution(clothes) {
    
    let hash = new Map();
    let result = 1;
    for(let cloth of clothes) {
        if(!hash.has(cloth[1])){
          hash.set(cloth[1],1)
        } 
        else{
            hash.set(cloth[1],hash.get(cloth[1]) + 1);  
        } 
        
    }
    
    for(let el of hash.values()){
        result *= (el+1)
    }


    return result-1
}
```

### 배운 점

```js
for(let el of hash.values()){
        result *= (el+1)
    }
```

ES6 `hash.values()`를 통한 value값 도출