## 버블 정렬 

**Concept** 

* 바로 가까이에 있는 두 숫자끼리 비교해서 당장 더 작은 숫자를 앞으로 보내주는 것을 반복

```js
function bubbleSort (array) {
  let temp;
  let arr = array;
  for(let i=0; i<arr.length; i++) {
    for(let j=0; j<arr.length - i; j++) {
      if(arr[j] > arr[j+1]){
        temp = arr[j]
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
  return arr;
}

bubbleSort([2,1,5,7,9,6,3,8,4])

// OutPut[1, 2, 3, 4, 5,6, 7, 8, 9]
```

### 시간 복잡도

**O(N^2);**

> 단순히 반복적으로 두 숫자를 비교하여 앞으로 보냅니다. 이 과정에서 각 싸이클마다 가장 큰 값이 맨 뒤로 보내지게 됩니다.
>  컴퓨터 내부적인 연산이 가장 비효율적으로 일어나게 되어 실제 수행시간이 가장 느린 안 좋은 알고리즘이라고 할 수 있습니다.