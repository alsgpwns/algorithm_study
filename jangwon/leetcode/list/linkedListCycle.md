# List

## 141. Linked List Cycle

### https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

* 풀이 1 (해시 이용)

```js
var hasCycle = function(head) {
    let set = new Set();
    
    while(head !== null) {
        if(set.has(head)) {
            return true;
        }
        set.add(head);
        head = head.next;
    }
    return false;
};
```

* 풀이 2 Two Pointer (Floyd's Cycle Finding Algorithm)

```js
var hasCycle = function(head) {
    let slow = head;
    let fast = head;
    
    while(fast && fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
        if(slow === fast) return true;
    }
    return false;
};
```

* 풀이 3 

```js
var hasCycle = function(head) {
    if(head === null){
        return false;
    }
    
    let slow = head;
    let fast = head.next;
    
    while(slow !== fast) {
        if(fast === null || fast.next === null){
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
};
```