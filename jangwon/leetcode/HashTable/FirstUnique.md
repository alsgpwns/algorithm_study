```js
/**
 * @param {number[]} nums
 */
class FirstUnique{
    constructor(nums){
        this.set = new Set();
        this.preDeleted = new Set();
        for(let q of nums){
            this.add(q);
        }
    }
    
    showFirstUnique(){
        for(let s of this.set){
            return s;
        }
        return -1;
    }
    
    add(val){
        if(this.set.has(val)){
            this.set.delete(val);
            this.preDeleted.add(val);
        }else if(!this.preDeleted.has(val)){
            this.set.add(val);
        }
    }
};
/** 
 * Your FirstUnique object will be instantiated and called as such:
 * var obj = new FirstUnique(nums)
 * var param_1 = obj.showFirstUnique()
 * obj.add(value)
 */

/*
    1) 요소가 첫번째로 유니크한 요소일 경우 반환
    2) 요소가 1개 이상이면 다음으로 넘어감  
    3) 모든 요소가 1개 이상인경우 -1 반환
    3) 요소를 넣을때 마다 hash를 갱신해주어야함!!

*/
```