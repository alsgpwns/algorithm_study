## 퀵 정렬

**Concept**

> 대표적인 **분할정복** 알고리즘으로 평균 속도가 O(N*logN)입니다.

* 퀵 정렬은 하나의 큰 문제를 두 개의 작은 문제로 분할하는 식으로 빠르게 정렬합니다. 
* 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나눕니다.

> 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나눕니다.

* 일반적으로 퀵 정렬에는 **기준 값(pivot)**이 있습니다. 이를 **피벗**이라고도 하는데, 보통 **첫 번째 원소** 를 피벗 값으로 설정하고 사용합니다.

### 알고리즘

* 피벗 값을 첫번째 요소로 설정합니다.
* 피벗값을 보다 큰 값과 작은 값을 찾습니다.
* 작은 값의 인덱스가 큰 값의 인덱스보다 작은 경우 (엇갈린 상황)
* 피봇 값을 작은 값과 자리를 바꿔 줍니다. (swap)

```js
function quickSort (array,start,end) {
  let arr = array;

  // 원소가 1개인 경우 
  if(start >= end) {
    return ;
  }

  // pivot:pivot는 첫번째 원소 

  let pivot = start;
  let i = start + 1 ;
  let j = end;
  let temp;

  // 엇갈릴때 까지 반복
  while(i <= j) {

    // 키 값보다 큰 값을 만날때까지 우측으로 이동 
    while(arr[i] <= arr[pivot]) {
      i++;
    }

    // 키 값보다 작은 값을 만날때까지 좌측 이동 
    while(arr[j] >= arr[pivot] && j > start) {
      j--;
    }

    // 현재 엇갈린 상태인 경우 키 값과 교체 
    if(i > j) {
      temp = arr[j];
      arr[j] = arr[pivot];
      arr[pivot] = temp;
    }else {
      temp = arr[j];
      arr[j] = arr[i];
      arr[i] = temp;
    }
  }

  quickSort(arr,start,j -1);
  quickSort(arr,j+1,end);

  return arr;
}

let array = [2,1,5,7,9,6,3,8,4]

quickSort(array,0,array.length-1);
```

**Js 내장메소드를 사용한 알고리즘 방식** 

```js
function quickSort (array) {
  if (array.length <= 1) {
    return array;
  }

  // 맨 첫 요소를 pivot으로 설정
  const pivot = [array[0]];
  const left = [];
  const right = [];
  for (let i = 1; i < array.length; i++) {

    // 피봇의 다음 요소가 피봇보다 작은 경우 왼쪽 배열에 담는다.
    if (array[i] < pivot) {
      left.push(array[i]);
    } 
    // 피봇보다 큰 경우 오른쪽 배열에 담는다.
    else if (array[i] > pivot) {
      right.push(array[i]);
    } else {  
     pivot.push(array[i]);
    }
}
  console.log(`left: ${left}, pivot: ${pivot}, right: ${right}`);
  return quickSort(left).concat(pivot, quickSort(right));
}
```

### 시간복잡도 

> 퀵정렬의 평균 시간 복잡도는 O(N*logN)입니다.
> 퀵정렬의 최악 시간 복잡도는 O(N^2)입니다.

이미 정렬이 되어있는 경우 분할 정복의 이점을 사용하지 못한다. 그렇기 때문에 최악의 시간복잡도인 O(N^2) 나오게 됩니다. 
