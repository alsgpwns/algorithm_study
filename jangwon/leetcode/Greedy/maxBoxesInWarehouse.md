```js
/**
 * @param {number[]} boxes
 * @param {number[]} warehouse
 * @return {number}
 */
var maxBoxesInWarehouse = function(boxes, warehouse) {
    let box = boxes.slice();
    let result = 0;
    
    if(warehouse.length === 0 || boxes.length === 0){
        return 0;
    }
    
    const recur = (box,warehouse) => {
        let bMax = Math.max(...box);
        let wMax = Math.max(...warehouse);
        if(bMax > wMax){
            for(let el of box){
                if(el === bMax){
                    const idx = box.indexOf(el);
                    box.splice(idx,1);
                }
            }
        }else{
            for(let el of box){
                if(el === bMax){
                    const idx = box.indexOf(el);
                    box.splice(idx,1);
                }
            }
            
            for(let el of warehouse){
                if(el === wMax){
                    const idx = warehouse.indexOf(el);
                    warehouse.splice(idx,1);
                }
            }
            result++;
        }
        
        // 탈출 조건 
        if(box.length === 0){
            return;
        }
        return recur(box,warehouse);
    }
    recur(box,warehouse);
    return result;
};

// 해당 인덱스를 삭제 

/*
    1) 스택의 크기 
    2) 창고의 인덱스가 스택의 크기이다. 
*/
```

* 풀이

1) Two Pointer

```js
/**
 * @param {number[]} boxes
 * @param {number[]} warehouse
 * @return {number}
 */

let maxBoxesInWarehouse = (box, w) => {
    box.sort((a,b)=>b-a);
    let cnt = 0;
    let i= 0;
    let j=w.length -1;
    for(let k=0; k<box.length && i<=j; k++){
        if(box[k] <= Math.max(w[i],w[j])){
            cnt++;
            if(w[i] > w[j]){
                i++;
            }else{
                j--;
            }
        }
    }
    return cnt
};

```