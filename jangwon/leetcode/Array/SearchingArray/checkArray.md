# Array

## Check If N and Its Double Exist

### https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

```js
var checkIfExist = function(arr) {
  let set = new Set();
  for (var a of arr) {
      if(set.has(a)) return true;
      set.add(a/2);
      set.add(a*2);      
  }

  return false;
};
```

```js
var checkIfExist = function(arr) {
    for(let i=0; i<arr.length; i++){
      for(let j=i+1; j<arr.length; j++){
        if(arr[i] === 2 * arr[j] || arr[j] === 2 * arr[i]) {
          return true
        }
      }
    }
  return false;
};
```

```js
var checkIfExist = function(arr) {

  let doubles = new Map();
  let n = arr.length;
  
  for (let i = 0; i < n; i++) {
    doubles.set(arr[i], i);
  }

  for(let j = 0; j < n; j++) {
    if(doubles.has(arr[j]*2) && doubles.get(arr[j]*2) !== j) {
      return true;
    }
  }
  
  return false;
```