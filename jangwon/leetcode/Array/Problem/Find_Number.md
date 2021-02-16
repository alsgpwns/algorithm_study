## Find Numbers with Even Number of Digits

* https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3237/

```js
var findNumbers = function(nums) {
    let count = 0;
    
    nums = nums.map((el)=>(el+""))
    
    nums.map((el)=>{
        if(el.length % 2 === 0){
            count++
        }
    })
    
    return count;
};
```