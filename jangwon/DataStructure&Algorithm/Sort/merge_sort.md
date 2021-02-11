## 병합 정렬 

**Concept**

> 일단 반으로 나누고 나중에 합쳐서 정렬하면 어떨까?

* 병합 정렬은 하나의 큰 문제를 두 개의 작은 문제로 분할한 뒤에 각자 계산하고 나중에 합니치는 방법을 채택합니다. 즉 기본 아이디어는 일단 **정확히 반으로 나누고 나중에 정렬하는 것입니다.**

* 병합 정렬은 퀵 정렬과는 다르게 피벗 값이 없고 항상 반으로 나눈다는 특징이 있습니다. 이 특징의 단계의 크기가 logN이 되도록 만들어줍니다.

* 병합 정렬은 합치는 순간에 정렬을 합니다.


```js
/* 병합 정렬 */
let array = [2,1,3,6,8,5,7];

function mergeSort(array) {
  let i,m,j,middle,k;

  let i = m;
  let j = middle + 1;
  let k = m ;

  // 작은 순서대로 배열에 삽입
  while (i <=middle && j <=n ){
    if(a[i] <= a[j]){
      sorted[k] = a[i];
      i++;
    }else{
      sorted[k] = a[j];
      j++;
    }
    k++;
  }

  // 남음 데이터 또한 삽입
  if(i > middle) {
    for(let i=j; i <=n; i++ ) {
      sorted[k] = a[i]
      k++
    }
  }else {
    for(let i=i; i <= middle; i++) {
      sorted[k] = a[i];
      k++
    }
  }

  // 정렬된 배열을 삽입
  for(let i=m; i<=n; i++) {
    a[i] = sorted[i];
  }
}

function mergeSortOutput (i,m,n) {
  // 크기가 1보다 큰경우 
  if( m < n ) {
    let middle = (m + n) / 2;
    mergeSort(a,m,middle);
    mergeSort(a,middle+1,n);
    merge(a,m,middle,n);
  }
}

```