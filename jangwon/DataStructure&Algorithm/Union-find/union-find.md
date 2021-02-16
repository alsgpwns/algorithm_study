# 합집합 찾기 (Union-Find)

**Union-Find(유니온-파인드)** 는 대표적인 **그래프** 알고리즘입니다. 바로 '합집합 찾기'라는 의미를 가진 알고리즘인데요. 서로소 알고리즘이라고도 부릅니다. 구제척으로 여러 개의 노드가 존재할 때 두 개의 노드를 선택해서, 현재 이 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘입니다.

**재귀함수**

```js

// 부모 노드를 찾는 함수
function getParent (array,value) {
  let parent = array;
  if(parent[value] === value) return value;
  return parent[value] = getParent(parent,parent[value]);
}

// 두 부모 노드를 합치는 함수
function unionParent(array,a,b) {
  let parent = array;
  const aRoot = getParent(parent,a);
  const bRoot = getParent(parent,b);
  if(aRoot < bRoot) parent[b] = a;
  else parent[aRoot] = bRoot;
}

// 같은 부모를 가지는지 확인

function findParent(array,a,b) {
  const aRoot = getParent(array,a);
  const bRoot = getParent(array,b);
  if( aRoot === bRoot ) return true;
  return false;
}

function main () {
  let parent = [];
  for(let i=0; i<=10; i++ ) {
    parent[i] = i;
  }

  unionParent(parent,1,2);
  unionParent(parent,2,3);
  unionParent(parent,3,4);
  unionParent(parent,5,6);
  unionParent(parent,6,7);
  unionParent(parent,7,8);

  console.log(`1과 2는 연결이 되어 있나요??` , findParent(parent,1,2))
}

main()
```