# 큐 

**Concept**

> 큐는 먼저 들어온 것이 먼저 나가는 구조를 가지고 있습니다. 실생활과 연관지어 은행 창구를 떠올릴수 있습니다.
> 먼저 번호표를 뽑은 사람이 먼저 서비를 받게 되고 중간에 새치기는 불가능한 것이 기본적인 큐의 구조입니다.

---


<img src="https://camo.githubusercontent.com/a98486bae83b4a5c7efcc361d1b1440d471c4d0f874b014aab59a7374b0fddf9/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f352f35322f446174615f51756575652e737667" />


## JS로 Queue 구현하기 (ES6)

* array를 사용하여 queue를 구현 할 수 있습니다. 
* array의 **push** 메소드로 enqueue를 , shift메소드로 dequeue를 구현 할 수 있습니다. 

```js
class Queue {
  constructor() {
    this.store = [];
  }

  enqueue(item) {
    this.store.push(item);
  }

  dequeue() {
    this.store.shift();
  }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.dequeue();   // 1
```