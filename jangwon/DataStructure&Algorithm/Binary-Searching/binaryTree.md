# 이진 트리의 구현과 순회 방식

* 기본적으로 가장 많이 사용되는 비선형 자료구조는 `이진트리`입니다. 이진 트리는 트리 자료구조를 활용한 대표적인 예시로 데이터의 탐색 속도 증진을 위해 사용하는 구조입니다. 

## 이진트리의 순회

1. 전위 순회(PreOrder Traversal) `C-L-R`
   * 하나의 노드에 방문했을 때 다음 순서를 따릅니다.
   1) 먼저 자기 자신을 처리합니다.
   2) 왼쪽 자식을 방문합니다. 
   3) 오른쪽 자식을 방문합니다.

2. 중위 순회(Inorder Traversal) `L-C-R`
   
   1) 왼쪽 자식을 방문합니다. 
   2) 자기 자신을 방문합니다. 
   3) 오른쪽 자식을 방문합니다.
   
3. 후위 순회(PostOrder Traversal) `L-R-C`
   
   * 후위 순회는 컴퓨터의 계산을 처리할 때 유용하게 쓰입니다.

   1) 왼쪽 자식을 방문합니다. 
   2) 오른쪽 자식을 방문합니다.
   3) 자기 자신을 방문합니다. 


```js
let Tree = (function() {

  function Tree() {
    this.count = 0;
    this.root;
  }

  function Node(data) {
    this.data = data;
    this.left;
    this.right;
  }

  function _insert(root, node) {
    if (!root) return node;
    if (node.data < root.data) {
      root.left = _insert(root.left, node);
      return root;
    } else {
      root.right = _insert(root.right, node);
      return root;
    }
    return root;
  }

  Tree.prototype.add = function(data) {
    var node = new Node(data);
    if (this.count == 0) {
      this.root = node;
    } else {
      _insert(this.root, node);
    }
    return ++this.count;
  };

  function _get(data, node) {
    if (node) {
      if (data < node.data) {
        return _get(data, node.left);
      } else if (data > node.data) {
        return _get(data, node.right);
      } else {
        return node;
      }
    } else {
      return null;
    }
  }

  Tree.prototype.get = function(data) {
    if (this.root) {
      return _get(data, this.root);
    } else {
      return null;
    }
  };
  
  function _remove(root, data) {
    var newRoot, exchange, temp;
    if (!root) return false;
    if (data < root.data) {
      root.left = _remove(root.left, data);
    } else if (data > root.data) {
      root.right = _remove(root.right, data);
    } else {
      if (!root.left) {
        newRoot = root.right;
        // root 메모리 정리
        return newRoot;
      } else if (!root.right) {
        newRoot = root.left;
        // root 메모리 정리
        return newRoot;
      } else {
        exchange = root.left;
        while (exchange.right) exchange = exchange.right;
        temp = root.data;
        root.data = exchange.data;
        exchange.data = temp;
        root.left = _remove(root.left, exchange.data);
      }
    }
    return root;
  }
  Tree.prototype.remove = function(key) {
    var node = _remove(this.root, key);
    if (node) {
      this.root = node;
      this.count--;
      if (this.count == 0) this.root = null;
    }
    return true;
  };
  return Tree;
})();
```