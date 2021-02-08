**문제3**

### 실패율

https://programmers.co.kr/learn/courses/30/lessons/42889

* 풀이

```js

   function solution(N, stages) {
    let arr =[];
    let totalMember = stages.length;
    
    for(let i=1; i<=N; i++) {
        let failMember = stages.filter((el)=>el===i).length;
        let failure=0;
        
        if(failMember === 0) {
            failure = 0;
        }else {
            failure = failMember / totalMember;
        }
        
        totalMember = totalMember - failMember;
        
        arr.push({idx:i, fail: failure})
    }
    
    arr.sort((a,b)=>{
        if(a.fail > b.fail) {
            return -1;
        }else if(a.fail < b.fail){
            return 1;
        }
        return 0;
    })
    
    return arr.map((el)=>el.idx);
    
}

// 실패율 구하기 

/*
    1) 스테이지의 길이로 전체 길이 구하기
    2) 스테이지의 사람 개수 구하기
    3) 스테이지의 길이를 사람으로 나눠주기
    4) 실패율을 구함
    5) 스테이지의 길이를 실패한 사람만큼 줄여주기 
    
    6) 반복 
    
    7) 정렬 

*/
```

* 삽질 풀이

```js
function solution(N, stages) {
    // 재귀
    
    // 실패율 구하기 
    
    const recur = (N,arr) => {
        let failArr = [];
        let min = Math.min.apply(null,stages);
        let count = 0;
        arr.map((el)=>{
            if(el === min) {
                count++
            }
        })
        let failaure = (count / arr.length);
        
        // 배열 같은 요소 제거 
        
       arr.filter((el,i,arr)=>{
           if(arr.includes(min)){
               const idx = arr.indexOf(min);
               arr.splice(idx,1);
           }
       })
        
        // 재귀 탈출 조건
        if(stages.length !==0){
            return recur(N,arr)
        } else return; 
    }
    
    recur(N,stages)
    
    
    
}





/* 문제 풀이

해시로 각 스테이지를 넣어주고 그에 따라 실패율 키를 할당해준다. 

해시의 키로 실패율을 비교하고 정렬해서 리턴한다. 

    1) 실패율 구하기 (재귀 함수 생성)
        
        * 배열에서의 최솟값을 구한다. (최솟값이 그 스테이지)
        * 최솟값의 개수가 몇개인지 구한다. 
        * 배열의 길이에서 최솟값의 개수를 나눠준다 (실패율)
        * 최솟값 요소를 모두 제거 해준다. (다음 실패율 구할 때)
    2) 실패율을 해쉬의 값으로 삽입해준다.
    
    3) 해쉬의 값을 비교한다. 
    
    4) 값대로 비교하여 정렬하고 
    
    5) 배열에 넣어주어 반환한다. 
    
    
    제한사항 
    만약 stage의 요소가 모두 같을경우 
*/


/*

문제 해석

스테이지 개수 N
사용자가 멈춰잇는 스테이지 번호가 담긴 배열 stages

실패율이 높은 스테이지부터 스테이지 번호가 담겨있는 배열을 return 

N+1은 마지막 스테이지 까지처리 

제한사항 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의 
*/

// 레퍼런스 배열 최솟값 , 최댓값 https://jayprogram.tistory.com/34
```