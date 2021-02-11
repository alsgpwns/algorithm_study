# Priority Queue(우선 순위 큐)

**Concept**

* Priority queue(우선순위 큐)는 선입 선출방식이 아닌, 우선순위를 기준으로 우선순위가 높은 요소를 먼저 삭제 하는 큐입니다. 
* 우선 순위가 같다면 큐에 삽입된 시점을 기준으로 삭제합니다.
* 배열, 연결리스트, 힙 기반으로 우선순위 큐를 구현할 수 있으며 각각의 시간 복잡도가 다릅니다.
* 배열과 연결리스트의 경우, 삽입을 위한 적절한 위치를 찾기 위해 모든 인덱스를 탐색해야하므로 최악의 경우 성능이 좋지 않을 수 있습니다. 하지만 구현이 간단하다는 장점이 있습니다. 

--- 

**배열 기반 우선순위 큐**

* 삽입:O(N)
* 삭제:O(1)

**연결리스트 기반 우선순위 큐**

* 삽입:O(N)
* 삭제:O(1)

**힙 기반 우선순위 큐**

* 삽입: O(logN)
* 삭제: O(logN)


## 배열 기반 Priority queue 구현하기 🐰
  
* **splice()** **메소드로 dequeue를 구현합니다.**

* Score가 높은 학생을 먼저 추출한다는 방식으로 Priority Queue를 구현하였습니다.

```js

class PriorityQueue {
  constructor() {
    this.store = [];
  }
  
  enqueue(item) {
    this.store.push(item);
  }
  
  dequeue() {
    let entry = 0;
    this.store.forEach((item, index) => {
      if (this.store[entry].score < this.store[index].score) {
        entry = index;
      }
    });
    return this.store.splice(entry, 1);
  }
}

class Student {
  constructor(name, score) {
    this.name = name;
    this.score = score;
  }
}

// student와 같이 우선순위의 아이템이 되는 클래스

class PriorityQueueElement {
  constructor(element, priority) {
    this.element = element;
    this.priority = priority;
  }
}

const priorityQueue = new PriorityQueue();
const pengsoo = new Student('Pengsoo', 10);
const kim = new Student('MJKim', 5);
const jangwon = new Student('jangwon', 3);

priorityQueue.enqueue(pengsoo);
priorityQueue.enqueue(kim);
priorityQueue.enqueue(jangwon);

priorityQueue.dequeue();
```