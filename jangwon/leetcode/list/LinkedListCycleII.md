# List

## Linked List Cycle II

### https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

```js
var detectCycle = function(head) {
    let map = new Map();
    
    while(head !== null) {
        if(map.has(head)){
            // 인덱스 반환
            return head;
        }
        map.set(head);
        head = head.next;
    }
    return null;
};
```