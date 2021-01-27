**풀이**

1. 요소를 divisor로 나눈다
2. 나누어떨어지는 값을 찾는다. 
3. 오름차순으로 정렬한다.
4. 반환한다.

```js
function solution(arr, divisor) {    
  let result = arr.filter((el)=> el % divisor === 0).sort((a,b) => a - b);
  return result.length === 0 ? [ -1 ]: result;
}

```

## 배운 것 

### 숫자 정렬

```js
  sort((a,b) => a - b)
}
```