# Array

## Replace Elements with Greatest Element on Right Side


**내 풀이** 

```js
var replaceElements = function(arr) {
    if(arr.length === 1) {
        return [-1];
    }
    
    for(let i=0; i <arr.length-1; i++){
        let maxNum = arr[i+1];
        for(let j=i+1; j < arr.length; j++) {
            if(arr[j] >= maxNum){
                maxNum = arr[j];
            }
        }
        arr[i] = maxNum;
    }
    
    arr[arr.length-1] = -1;
    
    return arr;
};
```