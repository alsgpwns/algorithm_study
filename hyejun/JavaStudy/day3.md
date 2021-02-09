# Day6 [Level1]
### 문제1 

![image](https://user-images.githubusercontent.com/45223821/106345386-1d1dcf80-62f3-11eb-9432-6b88dc49cbdd.png)
<https://programmers.co.kr/learn/courses/30/lessons/12928>
### 문제 설명
- 아주 간단하다.

- 정수 n의 모든 약수를 return해주면된다.
  

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106345387-1f802980-62f3-11eb-8152-beb5eb361020.png)

### 풀이
1. 정수 n까지 for문을 돌린다

2. n을 i로 나눌 수 있다면, 정수의 약수라고 판단하여, answer에 더해준다.

3. answer를 return 해주면 끝!
```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=n; i++) {
        	if(n%i==0) answer+=i;
        }
        return answer;
    }
}
```
---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106345407-51918b80-62f3-11eb-9c79-7292ad71eb72.png)

<https://programmers.co.kr/learn/courses/30/lessons/12917>

### 문제 설명
문제 그대로, 문자열을 내림차순으로 배열해주면된다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106345420-666e1f00-62f3-11eb-96bc-918de8d8bef4.png)


### 풀이
간단하다.

1. 문자열 sort

2. sort된 문자열을 역순으로 answer에 담아준다.
3. 
```java
import java.util.Arrays;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] temp= new String[s.length()];
         for(int i=0; i<s.length(); i++) {
        	temp[i] = s.charAt(i)+"";
        }
        Arrays.sort(temp);
        for(int i=s.length()-1; i>=0; i--) {
        	answer=answer+temp[i];
        }
        return answer;
    }
}

```
---
### 문제3 [partially completed]
체육복

<https://programmers.co.kr/learn/courses/30/lessons/42862>
### 문제 설명
 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
### 제한 사항
- 전체 학생의 수는 2명 이상 30명 이하입니다.
- 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106345462-ae8d4180-62f3-11eb-8ed1-b43b60486278.png)

### 풀이
1. 첫번 째 for문
   - stack에 lost 넣기

2. 두번 째 for문
    - int temp =stack.pop(); // stack의 맨 위 숫자를 temp에 넣음

3. 이중 for문
    - if(temp==reserve[j]+1 || temp==reserve[j]-1) // temp와 reserve배열의 value에 +1 한 값이 같다면
    - answer++; // count해준다 (++)
    - reserve[j] = 0; // 이중 체크 방지

3. 세번 째
    - answer = n - lost.length + answer; // answer구하는 공식(?) <- 맞는것같음!!

```java
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<Integer>();
        
        /* 첫번 째 */
        for(int i=0; i<lost.length; i++) {
        	stack.add(lost[i]);
        }
        
        /* 두번 째 */
        for(int i:stack) {
        	int temp =stack.pop();
        	for(int j=0; j<reserve.length; j++) {
        		if(temp==reserve[j] || temp==reserve[j]+1 || temp==reserve[j]-1) {
        			answer++;
        			reserve[j]=100;
        			break;
        		}
        	}
        }
        
        /* 세번 째 */
        answer=n-lost.length+answer;
        return answer;
    }
}
```