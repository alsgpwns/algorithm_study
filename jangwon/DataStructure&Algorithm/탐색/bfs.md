# 너비우선탐색 BFS

**Concept**
 
* 너비 우선 탐색(Breath First Search, BFS)은 탐색을 할때 너비를 우선으로 하여 탐색을 수행하는 탐색 알고리즘입니다. 특히나 '맹목적인 탐색'을 하고자 할 때 사용할 수 있는 탐색 기법입니다. 너비 우선 탐색은 '최단 경로'를 찾아준다는 점에서 최단 길이를 보장해야 할 때 많이 사용합니다. 준비물은 **큐(queue)** 입니다.

<p align="center">
  <img src="https://camo.githubusercontent.com/73761db9068bf4c9de4a23209da587a29e8cc672558534d4ff40ac0480854047/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f352f35642f427265616474682d46697273742d5365617263682d416c676f726974686d2e676966"/>
</p>

컴퓨터에는 그래프를 표현할수 있는 방법이 많지 않습니다. 이진법의 계산기를 사용하고 있고 그것을 입력하는 방법은 많지 않아 크게 두 가지로 나뉩니다. 두 가지 방법에는 **인접리스트와 인접행렬**이 있습니다.

**인접 리스트**

<p align="center">
  <img src="https://user-images.githubusercontent.com/33803975/107479954-2c3c3180-6bbf-11eb-99a0-f9f21fdee87f.png" />
</p>

  > 인접리스트의 장점은 공간효율성입니다. O(Edge)의 효율성만을 요구하기때문에 공간은 작게 차지하지만 시간의 효율성은 떨어집니다. O(Node)의 효율성이 들게 됩니다.

**인접행렬(그래프)**

<p align="center">
  <img src="https://user-images.githubusercontent.com/33803975/107480050-4e35b400-6bbf-11eb-8047-9425f6237ff9.png" />
</p>

  > 인접 행렬은 O(N^2)의 공간 효율성을 가지지만 시간 효율성은 O(1)밖에 되지 않기 때문에 시간효율성은 상당히 좋습니다.

**특징**

  - root와 가까운 node들부터 찾기 때문에 최단거리 탐색할 때 유용합니다.
  - queue에 각 노드의 정보를 기록해야하기 때문에 메모리를 많이 소모합니다.
  - **찾고자 하는 target이 root와 가까이 있다고 예상되는 경우에 BFS를 사용합니다.**
  - 지도 어플에서 특정 위치까지의 최단거리 안내, 혹은 소셜 미디어에서 친구 추천등에 어울립니다.


---


## BFS 예시

<p align="center">
<img src="https://user-images.githubusercontent.com/33803975/107480786-812c7780-6bc0-11eb-887c-7c7a2a54f4c4.png"
/>
</p>

**BFS 방식:  A - B - C - D - G - H - I - E - F - J**

### 그래프 BFS 알고리즘 구현

* 두 개의 큐(Queue)를 활용합니다.
  
```js

const graph = {
  A: ['B', 'C'],
  B: ['A', 'D'],
  C: ['A', 'G', 'H', 'I'],
  D: ['B', 'E', 'F'],
  E: ['D'],
  F: ['D'],
  G: ['C'],
  H: ['C'],
  I: ['C', 'J'],
  J: ['I']
};


const bfs = (graph,startNode) => {
  let visited = []; // 탐색을 마친 노드들 
  let needVisit = []; // 탐색을 해야할 노드들

  needVisit.push(startNode); // 노드 탐색 시작

  while(needVisit.length !==0) { // 탐색해야할 노드가 남아 있다면 
    const node = needVisit.shift(); // queue이기 때문에 선입선출, shift()를 사용한다.
    
    if(!visited.includes(node)) { // 해당 노드가 탐색 된 적이 없다면
      visited.push(node);
      needVisit = [...needVisit, ...graph[node]];
    }
  }
  return visited;
}
```

### 트리 BFS 


```js
class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySerachTree {
  constructor() {
    this.root = null;
  }

  // BFS
  BreathFirstSearch() {
    let currentNode = this.root;
    let list = [];
    let queue = []; // 방문 해야할 요소 큐 
    queue.push(currentNode);

    while(queue.length > 0) {
      currentNode = queue.shift();
      list.push(currentNode.value);

      if(currentNode.left) {
        queue.push(currentNode.left);
      }

      if(currentNode.right) {
        queue.push(currentNode.right);
      }
    }
    return list;
  }
}

// 순회 
function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}

```

### 트리 재귀 BFS 

```js
class Node {
  constructor() {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySerachTree {
  constructor() {
    this.root = null;
  }

  // BFS Recursive
  BreathFisrtSerachRecursive(queue,list) {
    if(!queue.length) {
      return list;
    }

    const currentNode = queue.shift();
    list.push(currentNode.value);

    if(currentNode.left) {
      queue.push(currentNode.left);
    }

    if(currentNode.right) {
      queue.push(currentNode.right);
    }

    return this.BreathFisrtSerachRecursive(queue,list);
  }
}

const tree = new BinarySearchTree();

const tree = new BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

console.log('BFS', tree.BreadthFirstSearch());

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
```