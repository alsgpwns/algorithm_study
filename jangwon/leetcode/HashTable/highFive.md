```js
/**
 * @param {number[][]} items
 * @return {number[][]}
 */
var highFive = function(items) {
    let s = {};
    let result = [];
    for(const [id,score] of items){
        if(!s[id]) {
            s[id] = [score];
        }else{
            s[id].push(score);
        }
    }
    const avg = (res,student) => {
        const topFive = s[student]
        .sort((a,b)=>b-a)
        .reduce((total,cur,idx) => {
            if(idx < 5) total += cur;
            return total;
        })
        res.push([student, Math.floor(topFive / 5)]);
        return res;
    }
    for(let el of Object.keys(s)){
        result.push(avg([],el))
    }
    console.log(result.flat(1));
    // return Object.keys(s).reduce(avg,[]);
};

/*
    1) 상위 5개의 평균을 구하기 
    
    1. 두개를 나눠서 정렬 
    2. 
*/