# 2020 카카오 인턴 

## 키패드 누르기

### https://programmers.co.kr/learn/courses/30/lessons/67256

* 내 풀이
  
1. 키패드의 위치를 좌표 배열인 객체로 만든다. 
2. 위치를 비교하여 왼쪽인지 오른쪽인지 반환하는 함수를 만든다. 
3. 조건에 따라 반환한다.


```js
function solution(numbers, hand) {
    let answer = "";
    
    const location = (pos,num,lhand,rhand,hand) => {
        const lD = Math.abs(pos[lhand][0] - pos[num][0]) + Math.abs(pos[lhand][1] - pos[num][1]);
        const rD = Math.abs(pos[rhand][0] - pos[num][0]) + Math.abs(pos[rhand][1] - pos[num][1]);
        
        if(lD === rD) return hand === 'left' ? 'L' : 'R';
        return lD < rD ? 'L' : 'R';
    }
    
    const pos = {
        1:[0,0], 2: [0,1], 3: [0,2],
        4:[1,0], 5: [1,1], 6: [1,2],
        7:[2,0], 8: [2,1], 9: [2,2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    
    let lhand = "*";
    let rhand = "#";
    
    for (let num of numbers){
        if ([1,4,7].includes(num)){
            answer += 'L';
            lhand = num;
        }        
        else if ([3,6,9].includes(num)){
            answer += 'R';
            rhand = num;
        }
        else{
            answer += location(pos,num, lhand, rhand, hand)
            answer[answer.length-1] === 'L'? lhand = num : rhand = num;
        }
    }
    return answer
}
```

**다른 사람 풀이**

> 모듈화

```js
function solution(numbers, hand) {
    const hands = new Map();
    let answer = "";
    hands.set("left", "*");
    hands.set("right", "#");

    numbers.forEach((number) => {
        if ([1, 4, 7].includes(number)) {
            answer += "L";
            hands.set("left", number);
        } else if ([3, 6, 9].includes(number)) {
            answer += "R";
            hands.set("right", number);
        } else {
            answer += findNearest(hands, number, hand);
        }
    });

    return answer;
}

function findNearest(hands, number, hand) {
    const keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"],
    ];

    const left = hands.get("left");
    const right = hands.get("right");
    let numIndex;
    let leftIndex;
    let rightIndex;

    keypad.forEach((arr, index) => {
        if (arr.includes(number)) numIndex = [index, arr.indexOf(number)];
        if (arr.includes(left)) leftIndex = [index, arr.indexOf(left)];
        if (arr.includes(right)) rightIndex = [index, arr.indexOf(right)];
    });

    const leftDistance = checkDistance(numIndex, leftIndex);
    const rightDistance = checkDistance(numIndex, rightIndex);

    if (leftDistance === rightDistance) {
        if (hand === "left") {
            hands.set("left", number);
            return "L";
        } else {
            hands.set("right", number);
            return "R";
            }
    } else {
        if (leftDistance < rightDistance) {
            hands.set("left", number);
            return "L";
        } else {
            hands.set("right", number);
            return "R";
        }
    }
}

function checkDistance(numIndex, hand) {
    if (numIndex[0] === hand[0]) {
        return Math.abs(numIndex[1] - hand[1]);
    }

    return (
        Math.abs(numIndex[0] - hand[0]) + Math.abs(numIndex[1] - hand[1])
    );
}
```