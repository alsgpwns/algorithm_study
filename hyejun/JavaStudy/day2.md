# Day2 [Brute-Forc/완전탐색]
### 문제
![carpet](https://user-images.githubusercontent.com/45223821/105562390-5091b480-5d5d-11eb-9789-b464d25dd442.PNG)

<https://programmers.co.kr/learn/courses/30/lessons/42842>

### 입출력 예
![입출](https://user-images.githubusercontent.com/45223821/105562530-e0cff980-5d5d-11eb-98ef-e6346341f1ff.PNG)

### 풀이
  
  * 여러 test case를 추가해서, 직접 그려보고 대입해보니 금방 풀 수 있었다.
  1. 기준이 될 변수와(height/i) 비교할 변수를(width/j) 만들어 값을 늘려가며 비교한다.
  2. width*height=carpet 이고, width*2 + height*2 -4의 값이 brown과 같다면, 정답으로 처리한다.
  3. 2번의 조건을 충족했을 때, 정답을 반환할 배열인 answer에 값을 넣고 for문을 break 해준다.

  ```java
    class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        int carpet = brown+yellow;
        
          for(int height=2; height<=carpet/2; height++) {
	        for(int width=3; width*height<=carpet; width++) {
	        	if( ((width*2 + height*2-4)==brown) && width*height==carpet ) {
	        		answer[0]=height;
	        		answer[1]=width;
	        		break;
	        	}
	        }
        }
        return answer;
    }
}
​
  ```
