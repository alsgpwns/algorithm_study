# String

## 657. Robot Return to Origin

* https://leetcode.com/problems/robot-return-to-origin/

* 내 풀이 

```js
var judgeCircle = function(moves) {
    let x = 0;
    let y = 0;
    
    for(let move of moves){
        switch(move){
            case "R":
            x++;
            break;
            case "L":
            x--;
            break;
            case "U":
            y++;
            break;
            case "D":
            y--;
            break;
        }
    }
    
    if(x === 0 && y === 0){
        return true;
    }
    return false;
};
```

* 다른 사람 풀이
  
```js
const judgeCircle = (moves) => {
  const map = moves.split('').reduce((map, c) => {
    return map.set(c, (map.get(c) | 0) + 1)
  }, new Map())
  return map.get('U') === map.get('D') && map.get('L') === map.get('R')
}
```

```js
const judgeCircle = (moves) => {
    return moves.split('')
        .reduce((p, m) => [p[0] + (m === 'R') - (m === 'L'), p[1] + (m === 'U') - (m === 'D')], [0, 0])
        .join('') === '00'
};
```