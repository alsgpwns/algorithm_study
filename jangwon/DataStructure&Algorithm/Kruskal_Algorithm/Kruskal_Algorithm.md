# 크루스칼 알고리즘(Kruskal Algorithm)

**Concept**

* 크루스칼 알고리즘은 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘 입니다. `최소 비용 신장 트리`를 만들기 위한 대표적인 알고리즘이라고 할 수 있습니다. 흔히 여러 개의 도시가 있을 때 각 도시의 도로를 이용해 연결 하고자 할 때 비용을 최소한으로 하고자 하는 경우 실제로 적용되는 알고리즘 입니다.

* 크루스칼 알고리즘에서 간선의 숫자는 노드의 숫자보다 한개가 적다. 노드를 모두 연결한 최소 간선을 구하는 것이기 때문에 노드의 개수에서 -1 한 값이 노드를 모두 연결한 최소 간선을 개수가 된다.
  * 간선(Edge)의 개수 = Node의 개수 -1 

> 간선을 거리가 짧은 순서대로 그래프에 포함 시키면 어떨까??

* 모든 노드를 최대한 적은 비용으로 `연결만` 시키면 되기 때문에 모든 간선 정보를 오름차순으로 정렬한 뒤에 비용이 적은 간선부터 차근 차근 그래프에 포함 시키면 되는 것입니다.

1. 정렬된 순서에 맞게 그래프에 포함 시킵니다.
2. 포함시키기 전에는 `사이클 테이블을 확인`합니다.
3. 사이클을 형성하는 경우 간선을 포함하지 않습니다.
   
여기서 사이클이라는 것은 그대로 그래프가 서로 연결되어 사이클을 형성하는 경우입니다. 최소 비용 신장트리에서는 `사이클이 발생`하면 안 됩니다. 애초에 모든 노드를 이어 붙이기만 하면 되는데 사이클이 발생할 이유가 없기 때문입니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/33803975/107896329-4e480200-6f79-11eb-976e-999e5e2ed630.png" width="80%">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/33803975/107896334-50aa5c00-6f79-11eb-8d52-74fac72be6fa.png" width="80%">
</p>

사이클의 발생 여부는 Union-Find 알고리즘을 그대로 적용하면 됩니다. 

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

// 간선 클래스 선언
// 간선의 비용을 기준으로 오름차순 정렬

// 각 정점이 포함된 그래프가 어디인지 저장
// 사이클이 발생하지 않는 경우 그래프에 포함

// class KrusKal {
//   constructor(nodes, edges) {
//     // 생성자를 통한 초기화
//     this.nodes = new unionfind(nodes);
//     this.edges = edges;
//     this.graph = [];
//   }

//   mst() {
//     while(this.edges.length > 0) {
//       this.findmin()
//     }
//     console.log(this.graph);
//   }

//   findmin(parent) {
//     // 엣지 오름차순 정렬 
//     this.edges.sort((a,b) => a-b);
//     let minWeight = this.edges.shift();
//     let result = this.nodes.unionParent(parent,minWeight[0],minWeight[1]);
//     if(result) {
//       this.graph.push(minWeight);
//     }
//   }
// }


```