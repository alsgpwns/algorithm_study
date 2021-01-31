**풀이 1** 

```js

// Math.min을 사용한 풀이 
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)) ,1)
    return arr.length === 0 ? [-1] : arr
}
```

**풀이 2**

```js
function solution(arr) {
    
    // 비교 순회 
    
    // 임시 변수 선언 
    let temp = 0;
    
    for (let j = 1; j<arr.length; j++){
        if(arr[j]<arr[temp]) {
            temp=j;
        }
    }
    
    arr.splice(temp,1);

    return arr.length === 0 ? [-1] : arr;
}
```



### 배운 점 

  * Math.min()
  * Math.max()

```Array.reduce()``` 이 함수 또한 배열의 각 값을 비교하여 가장 큰 숫자를 얻을 수 있습니다.

```js
var arr = [1,2,3];
var max = arr.reduce(function(a, b) {
    return Math.max(a, b);
});
```


```spread operator```이 함수를 사용하면 배열의 숫자들 중 가장 큰 숫자를 쉽게 얻을 수 있습니다.

```js
var arr = [1, 2, 3];
var max = Math.max(...arr);
```

### 레퍼런스

  * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max