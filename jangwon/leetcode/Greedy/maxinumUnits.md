
```js
var maximumUnits = function(boxTypes, truckSize) {
  let boxes = boxTypes.sort((a, b) => b[1] - a[1]);
  let units = 0, i = 0;
  for(let [count, num] of boxes) {
      if (count <= truckSize) {
          units += count * num;
          truckSize -= count;
          if (truckSize === 0) {
              break;
          }
      } else {
          units += truckSize * num;
          break;
      }
  }
  
  return units;
};
```

```js
var maximumUnits = function(boxTypes, truckSize) {
  let result = 0;
  boxTypes.sort((a, b) => a[1] - b[1]);
  
  while(truckSize > 0 && boxTypes.length > 0){
      const [num,units] = boxTypes.pop();
      console.log(num,units)
      result += (truckSize >= num ? num : truckSize) * units;
      truckSize -=num;
  }   
  return result;
}
```

### 풀이를 통해 배운 점

1. 2차원 배열의 정렬 ```boxTypes.sort((a, b) => a[1] - b[1]);```
2. 2차원 배열의 요소가 두개 인 경우 for of 문 활용 ```for(let [count, num] of boxes)```
3. 비구조화 배열 문법 ```const [num,units] = boxTypes.pop();```