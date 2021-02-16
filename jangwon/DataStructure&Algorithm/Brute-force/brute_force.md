# 완전 탐색 (Brute Force)

## 조합 

```js
arr : [1,2,3,4] 배열 
num: 3 4개 중 3개를 뽑음

function combination(arr, num) {
  let result = [];
  if(num == 1) return arr.map(e => [e]);
  
  arr.forEach((e,i,array) => {
    let rest = array.slice(i+1);
    let combinations = combination(rest,num-1);
    let combiArr = combinations.map(x => [e, ...x])
    result.push(...combiArr);
  }) 
  return result;
}
/* [ [ 1, 2, 3 ], [ 1, 2, 4 ],
   [ 1, 3, 4 ], [ 2, 3, 4 ] ] */
```

### 순열

```js
function combination(arr, num) {
  let result = [];
  if(num == 1) return arr.map(e => [e]);
  
  arr.forEach((e,i,array) => {
    let rest = [...array.slice(0,i), ...array.slice(i+1)];
    let combinations = combination(rest,num-1);
    let combiArr = combinations.map(x => [e, ...x])
    result.push(...combiArr);
  }) 
  return result;
}
/* [
  [ 1, 2, 3 ], [ 1, 2, 4 ],
  [ 1, 3, 2 ], [ 1, 3, 4 ],
  [ 1, 4, 2 ], [ 1, 4, 3 ],
  [ 2, 1, 3 ], [ 2, 1, 4 ],
  [ 2, 3, 1 ], [ 2, 3, 4 ],
  [ 2, 4, 1 ], [ 2, 4, 3 ],
  [ 3, 1, 2 ], [ 3, 1, 4 ],
  [ 3, 2, 1 ], [ 3, 2, 4 ],
  [ 3, 4, 1 ], [ 3, 4, 2 ],
  [ 4, 1, 2 ], [ 4, 1, 3 ],
  [ 4, 2, 1 ], [ 4, 2, 3 ],
  [ 4, 3, 1 ], [ 4, 3, 2 ]
] */
```

## 부분 집합 (멱집합)

N 개의 원소로 구성된 집합의 모든 부분 집합의 개수는 몇 개인가?

크기 N 인 집합의 모든 부분 집합은 공집합과 자신을 포함하여 2^N 개 만큼 존재합니다.

N개의 비트로 표현할 수 있는 2진수를 생성하면 부분 집합의 수 만큼 생성됩니다.

각 원소가 부분 집합에 포함 되었는지를 1 또는 0으로 표현한다.

![스크린샷 2021-02-09 오전 9 54 07](https://user-images.githubusercontent.com/33803975/107300374-c1a2cd00-6abc-11eb-9c22-83eb14797503.png)

표에서 보듯이 2^𝑛−1 까지에 속한 각 정수 값은 하나의 부분집합에 대응된다.

### 방법1.반복문 + 비트 연산

```js
비트연산자 활용
let arr = [1,2,3,4];
let result = [];

for(let i = 1; i < (1 << arr.length); i++) {
  	result.push([]);
	for(let j = 0; j < arr.length; j++) {
    	if(i & (1 << j)) result[i-1].push(arr[j])
    }
}
 /* [
  [ 1 ],          [ 2 ],
  [ 1, 2 ],       [ 3 ],
  [ 1, 3 ],       [ 2, 3 ],
  [ 1, 2, 3 ],    [ 4 ],
  [ 1, 4 ],       [ 2, 4 ],
  [ 1, 2, 4 ],    [ 3, 4 ],
  [ 1, 3, 4 ],    [ 2, 3, 4 ],
  [ 1, 2, 3, 4 ]
] */
```

### 방법2.조합을 이용한 구현 

### 방법3.재귀 호출

----


## 자바스크립트의 집합 (Set)

> 자바스크립트에서 집합(Set)이란 중학교 때 처음 배우는 바로 그 집합 개념이다. 이를 일반화해서 얘기하면 유한하고 구분되는 항목들의 그룹이라고 표현할 수 있다. 좀 더 엄밀히 얘기하자면 중복을 허용하지 않고 정렬되지 않은 항목들을 그룹이다. 따라서 정의에 맞게 그 용도 역시 항목의 유일성을 확인하는 것이다.


* **메서드**

* **Set.prototype.add(value)** : Set 객체에 주어진 값을 갖는 새로운 요소를 추가합니다. Set 객체를 반환합니다.
* **Set.prototype.clear()** : Set 객체에서 모든 요소를 제거합니다.

* **Set.prototype.delete(value)** : value와 관련된 요소를 제거하고 Set.prototype.has(value)가 이전에 반환했던 값을 반환합니다. Set.prototype.has(value)는 그 뒤에 false를 반환합니다.

* **Set.prototype.forEach(callbackFn[, thisArg])** : 삽입 순으로 Set 객체 내에 있는 각 값에 대해 한 번 callbackFn을 호출합니다. thisArg 매개변수가 forEach에 제공된 경우, 이는 각 콜백에 대해 this 값으로 사용됩니다.

* **Set.prototype.has(value)** : Set 객체 내 주어진 값을 갖는 요소가 있는지를 주장하는(asserting, 나타내는) boolean을 반환합니다.
* 
* **Set.prototype.keys()** : values() 함수와 같은 함수로 삽입 순으로 Set 객체 내 각 요소에 대한 값을 포함하는 새로운 Iterator 객체를 반환합니다.

* **Set.prototype.values()** : 삽입 순으로 Set 객체 내 각 요소에 대한 값을 포함하는 새로운 Iterator 객체를 반환합니다.

```js
let set1 = new Set([1,2,3]);
let set2 = new Set('123');
console.log(set1); // {1,2,3};
console.log(set2); // {"1","2","3"};
```

* 삽입 삭제 
 
```js
let set1 = new Set([1,2,3])
set1.add(3) //{1,2,3}
set1.add(4) //{1,2,3,4}
set1.delete(4) //{1,2,3} && return true
set1.delete(4) //{1,2,3} && return false

console.log(set1)
```

> 집합 원소에 대해 add() 메소드를 이용해서 삽입을, delete() 메소드를 이용해서 삭제를 진행할 수 있다. delete() 메소드는 삭제의 성공 여부를 boolean으로 반환한다. 이때 삽입과 삭제의 시간복잡도는 O(1)인데, 자바스크립트 집합의 구현이 **해시테이블에** 근간을 두고 있는 덕분이다.

* 포함 여부

```js
let set1 = new Set([1,2,3])
set1.has(1) //true
set1.has(4) //fasle
```

**위에서 알아본 집합 클래스의 기본 기능들을 가지고 조금 더 응용된 집합 연산을 구현할 수도 있다.**

---- 

### 교집합

```js

function intersectSets(setA,setB) {
  let intersection = new Set();
  setB.forEach((el)=>{
    if(setA.has(el)) intersection.add(el);
  })
  return intersetcion
}

let setA = new Set([1,2,3]);
let setB = new Set([2,3,4,5]);

console.log(interSectionSets(setA,setB)); //Intersection: {2,3}
```

> 하나의 집합에 대해 모든 원소를 탐색하면서 나머지 집합이 해당 원소를 가졌는지 체크해주면 된다. 새로운 집합을 하나 만들어두고 공통 요소로 판명된 것들을 여기에 차곡차곡 넣어서 반환하면 그게 바로 교집합일 것이다.

### 합집합

```js
function unionSet(setA, setB) {
  let union = new Set(setA);
  setB.forEach((el)=>{
    union.add(el)
  })
}

let setA = new Set([1,2,3]);
let setB = new Set([2,3,4,5]);
console.log(unionSet(setA,setB)) //{1,2,3,4,5}

```

### 차집합

```js
function differenceSet(setA, setB){
  let difference = new Set(setA)
  setB.forEach(el=>{
    difference.delete(el)
  })
  return difference
}

let setA = new Set([1,2,3])
let setB = new Set([2,3,4,5])

console.log(differenceSet(setA,setB)) //{1}
console.log(differenceSet(setB,setA)) //{4,5}
```

> 합집합의 add() 메소드를 차집합에서는 delete()로 바꾸어주면 된다. 원리는 동일하다. 한가지 주의할점은 A U B 와 B U A 는 결과가 동일하지만 **A - B** 와 **B- A** 는 서로 다르다는 점이다. 덧셈은 순서가 바뀌어도 무방하지만 뺄셈에서는 순서가 절대적으로 중요한 것과 같은 이치이다. 따라서 함수를 사용할 때 인자의 순서에 신경을 써주어야 할 것이다.

### 부분집합

```js
function isSubSet(superSet, SetA) {
  let result = true;
  setA.forEach((el)=>{
    if(!superSet.has(el)) result = false;
  })
  return result;
}

let setA = new Set([1,2,3])
let setB = new Set([2,3,4,5])
let setC = new Set([1,2])

console.log(isSubSet(setA, setB)) //false
console.log(isSubSet(setA, setC)) //true
```



#### reference 

* https://makasti.tistory.com/99
* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set