# 두 정수 사이의 합 
https://programmers.co.kr/learn/courses/30/lessons/12912

### 문제 풀이 

- 반복문을 통한 풀이 

1. a와 b사이에 값을 구하는것이기 때문에 반복문을 통해 값을 누적시켜 풀었다. 

**풀이 1)**

```js
function solution(a, b) {
    
    let result = 0;
    
    if(a < b) {
        for (let i = a; i <= b; i++) {
            result = result + i
        }
    }else {
        for(let i = b; i <= a; i++){
            result = result + i
        }
    }
    return result ; 
```
}

* **시간복잡도 O(N)**

    for문 한바퀴 돌기 때문에 시간복잡도가 O(N)으로 나온다. 

# 문자열 p와 y의 개수 
https://programmers.co.kr/learn/courses/30/lessons/12916

### 문제 풀이

- 카운트 변수를 직접 만들어서 풀이 
  
    1. 문자열인 변수를 배열로 만들어 내장메소드를 사용 할 수 있게 처리 ```split()```
    2. 대소문자 구분이 없기 때문에 모두 소문자로 바꾸어줌 ```toLowerCase()```
    3. p와 y가 둘 다 없는 경우의 조건을 ```includes()``` 배열 내장메소드를 사용해 처리
    4. ```for of```를 사용하여 배열의 요소를 순회하고 타겟 요소가 있는 경우 count변수의 값을 한개씩 늘려줌
    5. 두 개의 카운트 변수인 countP, countY를 비교하여 결과값을 도출 

```js
function solution(s){
    let arr = s.split("")
    let countP = 0;
    let countY = 0;
    let result = [];
    
    
    arr.map((el)=>{
        result.push(el.toLowerCase());
    });
    
    // p와 y가 둘 다 없는 경우 조건 
    if(!result.includes("p") && !result.includes("y")){
       return true;
    }else{
        // 배열 요소를 순회해 count를 늘린다. 
        for(let el of result){
            if(el === "p"){
                countP++
            }
        }
        
        for(let el of result){
            if(el === "y"){
                countY++
            }
        }
    }
    
    // count를 비교 
    if(countP === countY){
        return true
    }

    return false;
}
```
* **시간 복잡도 O(N)**    

수정 풀이

```js
function solution(s){
    let countP = 0;
    let countY = 0;
    s = s.toLowerCase("").split("")
    
    for(let i = 0 ; i <s.length; i++){
        if(s[i] === "p") {
            countP++
        }
        if(s[i] === "y"){
            countY++
        }
    }
    
    return (countP === countY ? true:false)
}
```

### 레퍼런스 풀이 

**풀이1)**

```js
function numPY(s){
    return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}
```

length로 길이를 대체해서 한줄 코드로 풀이

**풀이2)**

```js
function numPY(s) {
  return s.match(/p/ig).length == s.match(/y/ig).length;
}
```

match 메소드와 정규표현식을 통한 풀이

**풀이3)**

나와 비슷한 풀이

```js
function numPY(s){
  var result = true;
  s = s.toUpperCase();
  var num = 0;
  for(var i = 0; i < s.length; i++){
    if(s[i] === 'P') num++;
    if(s[i] === 'Y') num--;
  }
  result = (num === 0);

  return result;
}
```

```js
function numPY(s){
  var result = true;
  var pCount = 0;
  var yCount = 0;
  s = s.toLowerCase();

  for(var i = 0; i < s.length ; i++) {
    if (s[i] === 'p') {
        pCount++;
    } else if (s[i] === 'y') {
        yCount++; 
    } 
  } 

  return (pCount === yCount) ? true : false;
}
```




### Reference

- [for-in문][https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/for...in]

- [for-of문][https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/for...of]


- [정규표현식][https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/%EC%A0%95%EA%B7%9C%EC%8B%9D]

- [match][https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/match]
