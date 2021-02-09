### 문제 2

**다리를 지나는 트럭**

https://programmers.co.kr/learn/courses/30/lessons/42583

```js
function solution(bridge_length, weight, truck_weights) {
    let result = [];
    let bridgeArr = [];
    
    for(let i=0; i< truck_weights.length; i++) {
        bridgeArr.push(truck_weights[i]);
        if(truck_weights[i] + truck_weights[i+1] > weight) {
            truck_weights.shift();
            let runtime = bridge_length;
            let count = 0;
            while(bridgeArr.length <= 0) {
                if(runtime > 0){
                 runtime -= 1;
                 count++   
                }else {
                  bridgeArr.shift();
                }
            }
            result.push(count);
        }
        
        // 두친구가 같이 탔을경우
        if(truck_weights[i] + truck_weights[i+1] < weight) { 
            
        }
    }
}


// 다리 길이 - 1초 * 2
```