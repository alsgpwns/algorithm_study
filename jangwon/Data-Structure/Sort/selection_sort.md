## 선택 정렬 

**Concept**

* 배열을 순회해서 가장 작은 수를 가장 앞으로 정렬하는 방법

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
}

selectionSort([2,1,5,7,9,6,3,8,4])
```

### 시간 복잡도 계산

> array 10 배열의 길이가 10일 경우
> 10 + 9 + 8 ... 1 = 55;
> 등차수열 n(n+1)/2 => O((n^2 + n + 1)/2)
> 가장 큰 n 
> O(n^2)