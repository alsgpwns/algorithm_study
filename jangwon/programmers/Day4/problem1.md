
### 문제 풀이

 1. 주어진 문자열을 배열로 바꿔주기위해 ```split()``` 함수를 사용하여 바꿔준다. 
 2. 문자열을 유니코드로 바꿔준다. ```charCodeAt()``` 사용 
 3. 소문자와 대문자를 비교해준다. 
 4. 그대로 반환 한다. 


```js
function solution(s, n) {

  // 배열로 만들어 줌 
    return s.split("").map((str) => {
      // 암호화 코드 생성 + n 
      const code = str.charCodeAt() + n;
          if(str.charCodeAt() >= "a".charCodeAt() && str.charCodeAt() <= "z".charCodeAt()) {
              if(code > "z".charCodeAt()) return String.fromCharCode(code -26);
              return String.fromCharCode(code);
          }

          if(str.charCodeAt() >= "A".charCodeAt() && str.charCodeAt() <= "Z".charCodeAt()) {
              if(code > "Z".charCodeAt()) return String.fromCharCode(code -26);
              return String.fromCharCode(code);
          }
          return " ";
      }).join("");
}
```

### 배운 점 

* ```charAt()```
  * 특정 인덱스에 위치하는 유니코드 단일 문자를 반환하는 함수

* ```fromCharCode()```
  * 유니코드를 문자열로 바꿔는 함수

* ```charCodeAt()```
  * 문자열을 유니코드로 바꾸는 함수   



### 레퍼런스

**문자열을 숫자로 바꾸기**

* https://stackoverflow.com/questions/22624379/how-to-convert-letters-to-numbers-with-javascript

**문자열 to 숫자** 

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/charAt

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode
