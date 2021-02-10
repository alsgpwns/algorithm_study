# Day10 [완전 탐색]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/107402102-f3f90c80-6b46-11eb-90db-968895bff081.png)



<https://programmers.co.kr/learn/courses/30/lessons/42842>


### 풀이
여러 test case를 추가해서, 직접 그려보고 대입해보니 금방 풀 수 있었다.
내가 푼 알고리즘은 다음과 같다.

​

-  변수

    carpet = brown+yellow : 전체 카펫의 크기

    width = 가로의 길이

    height = 세로의 길이

- 알고리즘

    1. 기준이 될 변수와(height/i) 비교할 변수를(width/j) 만들어 값을 늘려가며 비교한다.​

        ※ width*height의 값이 carpet 보다 절대 클 수 없으니, width의 범위를 아래와 같이 정한다.

        ※ width가 for문 아래에 선언되어 있어, width변수를 쓸 수 없다. 때문에 height의 범위를 아래와 같이 정했다.

    ​

    2. width*height=carpet 이고, width*2 + height*2 -4의 값이 brown과 같다면, 정답으로 처리한다.​

        ※ 여기서 width*2+height*2-4의 값은 brown과 같다. (사각형 겉면의 값)

    ​

    3. 2번의 조건을 충족했을 때, 정답을 반환할 배열인 answer에 값을 넣고 for문을 break 해준다.
    4. 

```java
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        int carpet = brown+yellow;
        
          for(int height=2; height<=carpet/2; height++) {
	        for(int width=3; width*height<=carpet; width++) {
	        	if( ((width*2 + height*2-4)==brown) && width*height==carpet) {
	        		answer[0]=height;
	        		answer[1]=width;
	        		break;
	        	}
	        }
        }
        return answer;
    }
}
```
### 다른 풀이
※ 다른 사람의 풀이와 비교해보니, 다들 비슷한것 같아서 이번 포스팅에선 다른사람의 풀이를 다루지 않겠다. 

---
### 문제2
소수 찾기

<https://programmers.co.kr/learn/courses/30/lessons/42839>


### 풀이
생각한 알고리즘
1. 모든 조합을 구한다
2. 구한 조합에서 소수를 판별한다.

조합을 구하는 코드를 짜보았는데, 결국 스스로 짜는건 실패했다.
자바에 조합을 구하는 library가 없어서 메소드를 찾아 다시 풀어봐야겠다.