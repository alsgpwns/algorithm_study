# String

## 1678. Goal Parser Interpretation

* https://leetcode.com/problems/goal-parser-interpretation/

```js
var interpret = function(command) {
    return command.replace(/\(\)/g,"o").replace(/\(al\)/g,"al");
};
```