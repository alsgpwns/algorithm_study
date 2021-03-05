# List

## 141. Linked List Cycle

### https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

* 풀이 

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

```js
var hasCycle = (head) => {
    let p1 = head;
    let p2 = head;
    
    while(p2 && p2.next && p2.next.next) {
        p1 = p1.next;
        p2 = p2.next.next;
        
        if(p1 === p2) {
            return true;
        }
    }   
    return false;   
}
```