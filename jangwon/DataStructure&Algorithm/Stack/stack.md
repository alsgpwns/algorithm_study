## JavaScript로 Stack 구현하기 (ES6) 😆

```js
class Stack {
  constructor() {
    this.store = [];
  }
  
  push(item) {
    this.store.push(item);
  }
  
  pop() {
    return this.store.pop();
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.pop();   // 2

```

## Queue 2개로 Stack 구현하기 

* Main Queue 와 Sub Queue 두개를 둔다.
* Main Queue 가 비었을 때는 item 을 바로 enqueue 하고,
* 그렇지 않을 때는 Main Queue 의 요소들을 Sub Queue 로 모두 옮겨서 비운 다음에 item 을 enqueue 한다. 이후 Sub 에 있는 요소들을 다시 Main 으로 옮긴다.

```js
class Queue {
  constructor() {
    this.store = [];
  }
  
  enqueue(item) {
    this.store.push(item);
  }
  
  dequeue() {
    return this.store.shift();
  }
  
  empty() {
    return (this.store.length === 0);
  }
}

class Stack {
  constructor() {
    this.main = new Queue();
    this.sub = new Queue();
  }
  
  push(item) {
    if(this.main.empty()) {
      this.main.enqueue(item);
    } else {
      while(!this.main.empty()) {
        this.sub.enqueue(this.main.dequeue());
      }
      this.main.enqueue(item);
      while(!this.sub.empty()) {
        this.main.enqueue(this.sub.dequeue());
      }
    }
  }
  
  pop() {
    this.main.dequeue();
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.pop();
console.log(stack.main.store);   // [2, 1]
```

### Stack 2개로 Queue 구현하기
* 데이터를 쌓을 스택 InStack, 데이터를 추출할 스택 OutStack 을 만듭니다.
* enqueue 액션이 발생하면, InStack 에 데이터를 쌓습니다.
* dequeue 액션이 발생하면, OutStack 에 있는 요소를 반환합니다.
* 이때, OutStack 이 비어 있다면, InStack 의 요소들을 OutStack 으로 모두 옮긴 다음, OutStack 에서 하나를 추출해서 반환합니다.
  
```js
class Stack {
  constructor() {
    this.store = [];
  }
  
  push(item) {
    this.store.push(item);
  }
  
  pop() {
    return this.store.pop();
  }
}

class Queue {
  constructor() {
    this.inStack = new Stack();
    this.outStack = new Stack();
  }
  
  enqueue(item) {
    this.inStack.push(item);
  }
  
  dequeue() {
    if (this.outStack.store.length === 0) {
      while(this.inStack.store.length > 0) {
        this.outStack.push(this.inStack.pop());
      }
    }
    return this.outStack.pop();
  }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);

queue.dequeue();   // 1  
```