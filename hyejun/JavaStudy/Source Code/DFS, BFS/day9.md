# Day9 [Level2/스택/큐]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/107254187-694adb80-6a7a-11eb-8468-26e18b48aa2c.png)
### 문제 설명
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


제한 사항
- 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

### 풀이
1. 날짜를 계산해 dayQue에 넣어준다.

2. top_num ( 제일 상단의 숫자)와 num(밑의 숫자)를 비교한다.

    2-1. 비교했을 떄 top_num이 크다면 num을 remove해주고, num을 peek해주고, count++해준다.

3. top_num이 num보다 작다면, 한 칸 아래의 top_num을 poll해주고, 한 칸 아래의 num을 peek해준다.

4. dayQue가 비어있지 않을 떄 까지 2~3을 반복한다.

5. answerArray를 retrun한다.
```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
         int num=0, top_num=0;
        Queue<Integer> dayQue = new LinkedList<>();
        ArrayList<Integer> answerArray = new ArrayList<>();
        

        //날짜 입력
        for(int i=0; i<progresses.length; i++) {
        	int temp = (int) Math.ceil((100-progresses[i])/(double)speeds[i]);
        	dayQue.add(temp);
        }
        
        //날짜 비교
        while(!dayQue.isEmpty()) {
        	int count=1;
        	top_num = dayQue.poll();
        	if(!dayQue.isEmpty()) num = dayQue.peek();
        	
        	while(top_num>=num && !dayQue.isEmpty()) {
        		dayQue.remove();
        		if(!dayQue.isEmpty()) num = dayQue.peek();
        		count++;
        	}
        	answerArray.add(count);
        }
        return answerArray;
    }
}
```
### 다른 풀이
1. 날짜를 계산해 변수 temp에 넣어준다.

2. if( dayQue가 비어있지 않고, dayQue의 가장 위 숫자가(peek) temp보다 작다면) 

list에 dayQue를 넣어주고, Que를 비워준다.(clear)

3. 2번을 충족하지 않는다면, Que에 temp값을 넣어준다.

4. 2~3을 progresses.length만큼 반복한다.

5. list에 dayQue를 add해준다.
```java
Class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> dayQue = new LinkedList<>();
        List<Integer> answerList = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
        	int temp = (int) Math.ceil((100-progresses[i])/(double)speeds[i]);

            if (!dayQue.isEmpty() && dayQue.peek() < temp) {
                answerList.add(dayQue.size());
                dayQue.clear();
            }
            dayQue.offer(temp);
        }

        answerList.add(dayQue.size());

        int[] answer = new int[answerList.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
```





---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/107253233-75826900-6a79-11eb-906d-c7965165fcda.png)
<https://programmers.co.kr/learn/courses/30/lessons/42583>

### 문제 설명
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.


제한 조건
- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

### 풀이
```java
import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
       Queue<Integer> queue = new LinkedList<>();
		int sum=0;
		for(int t: truck_weights) {
			while(true) {
				if(queue.isEmpty()) {
					queue.add(t);
					sum +=t;
					answer++;
					break;
				} else if(queue.size()==bridge_length) {
					sum=sum-queue.poll();
				} else {
					if(sum+t>weight) {
						answer++;
						queue.add(0);
					} else {
						queue.add(t);
						sum+=t;
						answer++;
						break;
					}
				}
			}
		}
		return answer + bridge_length;

    }
}
```
---
### 문제3
집중이 잘 안돼서 다 풀지 못했습니다.
주말에 풀이 완성해서 올리겠습니다.