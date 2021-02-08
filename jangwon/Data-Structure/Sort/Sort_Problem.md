# 백준 sort 문제


**수 정렬하기**

https://www.acmicpc.net/problem/2750

```js
function selectionSort (array) {
  let index,min,temp = 0;
  let arr = array;
  
  for(let i=0; i<arr.length; i++) {

    // 최솟값을 수에서 가장 큰 수로 가정 
    min = Infinity
    for(let j=i; j < arr.length; j++) {
      if(min > arr[j]) {
        min = arr[j];
        index = j;
      }
    }

    //swap 과정 
    temp = min;
    arr[index] = arr[i];
    arr[i] = temp
  }

  return arr;
```