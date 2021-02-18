# 탐욕법

## 큰 수 만들기

```js
function solution(number, k) {
    
    let arr = number.split("");
    let result = [];
    let subtract = number.length - k;
    
    // 조합 
    const getCombinations = function (arr, selectNumber) {
      const results = [];
      if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

      arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1); // 해당하는 fixed를 제외한 나머지 뒤
        const combinations = getCombinations(rest, selectNumber - 1); // 나머지에 대해서 조합을 구한다.
        const attached = combinations.map((combination) => [fixed, ...combination]); //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
        results.push(...attached); // 배열 spread syntax 로 모두 다 push
      });

      return results; // 결과 담긴 results return
    }
    
    let combinations = getCombinations(arr,subtract);
    
    for(let i=0; i<combinations.length; i++) {
        result.push(combinations[i].reduce((acc,val)=>acc+val))
    }
    
    return Math.max(...result) + "";
}

> 기본 테스트와 출력은 통과 하지만 런타임 에러로 테스트 케이스를 모두 통과하지 못했습니다.
> number의 데이터가 `1 ~ 10000000` 이기 때문에 시간 복잡도 O(N^2)으로 해결 해야하지만 시간복잡도가 재귀를 통해 그 이상으로 나오는것을 확인 할 수 있습니다. 추 후 수정

/*

 1) 조합으로 수를 구성 (배열)
 2) 조합 배열의 요소를 모두 더해 값 구함
 3) 결과 값중 가장 큰 값을 반환 

*/
```

### 레퍼런스

* https://jun-choi-4928.medium.com/javascript%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-21df4b536349