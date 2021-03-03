# String

## 1436. Destination City

* https://leetcode.com/problems/destination-city/
  
```js
var destCity = function(paths) {
    let hashMap = new Map();
    let result = [];
    let destination = ""
    
    for(let path of paths){
        for(let destination of path ){
            if(!hashMap.has(destination)){
                hashMap.set(destination,1);
            }else{
                hashMap.set(destination,hashMap.get(destination) + 1);
            }
        }
    }
    
    for(let el of hashMap){
        if(el[1] === 1){
            result.push(el[0]);
        }
    }
    
    paths.map((el,i)=>{
        el.map((ele,idx)=>{
           if(ele === result[0] && idx === 1 || ele === result[1] && idx === 1){
               destination = ele;
           }
        })
    })
    
    return destination;
};
```

```js
const destCity = (paths) => {
  const map = new Map();
  for (const path of paths) {
    map.set(path[0], map.has(path[0]) ? 0 : 1);
    map.set(path[1], map.has(path[1]) ? 0 : -1);
  }
  for (const item of map) {
    if (item[1] === -1) return item[0];
  }
};
```