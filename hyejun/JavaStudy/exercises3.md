# Day3 [Stack/Queue]
### 문제
![ㅈㅅㄱㄱ](https://user-images.githubusercontent.com/45223821/105685036-ff3e1c80-5f38-11eb-8af3-ee1b210ece49.PNG)

<https://programmers.co.kr/learn/courses/30/lessons/42584>

### 입출력 예
![입출](https://user-images.githubusercontent.com/45223821/105685391-5b08a580-5f39-11eb-90a3-2a962bf4fa17.PNG)

### 입출력 예 설명
- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

### 풀이
1. prices 배열의 0번째 요소부터 마지막 요소까지 비교한다.
2. 0번째 요소 => 1,2,3,4요소와 비교 / 1번째 요소 => 2,3,4요소와 비교해야 하므로, 
   - 비교하는 기준 요소를 두고, 요소를 한칸씩 뒤로 움직이며, 기준요소와 비교한다.
3. 기준요소(i)와 비교요소(j)를 비교했을 때, 
   -  i가 작다면 주식 가격이 떨어지지 않은것 이므로 answer[i]++;
   -  i가 크다면 주식 가격이 떨어진 것이므로 answer[i]++,주식 가격이 떨어졌다면 더이상 비교할 필요가 없으므로 break;
4. 최종 답안인 answer에 변수 count를 대입한다.

```java
    class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for(int i=0; i<prices.length; i++)
        {
        	int count=0;
        	for(int j=i+1; j<prices.length; j++)
        	{
        		if(prices[i]<=prices[j]) count++;
        		else if(prices[i]>prices[j]) { 
        			answer[i]= count++;
        			break;
        		}
        	}
        	answer[i]= count;
        }
        return answer;
    }
}
​
  ```

  ### 다른 풀이
  - 위에서 풀었던 answer[i]=count와 다르게 count 변수 없이, 바로 answer[i]++;을 해줌으로 같은 결과를 낸다.
  ```java
  for(int i=0; i<prices.length; i++)
{
        	for(int j=i+1; j<prices.length; j++)
        	{
        		answer[i]++;
        		if(prices[i]>prices[j]) break;
        	}
}
  ```

  ### 블로그
  <https://blog.naver.com/5550304/222206229545>
