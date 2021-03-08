# Day16 [카카오/시뮬레이션]
## 문제


![image](https://user-images.githubusercontent.com/45223821/110153563-8fb82880-7e26-11eb-9a24-48bda3d9a5a1.png)


<https://programmers.co.kr/learn/courses/30/lessons/67256>


## 이해

![image](https://user-images.githubusercontent.com/45223821/110153571-9181ec00-7e26-11eb-8727-846ee51142c2.png)

이 전화 키패드에서 왼손과 오른손의 엄지 손가락만을 이용해 숫자만을 입력하려고한다.

​

1. 초기 왼손 위치는 * 에, 오른손 위치는 # 에 위치한다.

2. 엄지 손가락은 상하좌우 4방향으로 이동할 수 있으며, 키패드 한 칸은 거리로 1에 해당한다.

3. 왼쪽열의 3개 숫자 1,4,7은 왼쪽 엄지 손가락을 사용한다.

4. 오른쪽열의 3개 숫자 3,6,9를 입력할 떄는 오른쪽 엄지 손가락을 사용한다.

5. 가운데 열의 4개 숫자 2 5 8 0을 입력할 때는 두 엄지손가락의 현재 키패드 위치에서 더 가까운 엄지 손가락을 사용한다.

    5-1. 만약, 두 엄지 손가락의 거리가 같다면, 오른손잡이는 오른쪽 손가락, 왼손 잡이는 왼쪽 손가락을 사용해 움직인다.




## 풀이
우선 이 문제는 크게 3가지 경우로 나뉜다.

1. 왼손이 Left버튼을 누르는 경우

2. 오른손이 Right를 누르는 경우

3. 그 외(Center)를 누르는 경우

3번의 경우, 왼손과 오른손의 최단거리를 구해, 더 가까운 쪽을 선택하게 했다.

최단 거리는 이중좌표를 이용해, "맨해튼 거리"식으로 구했다. ( |x1-x2| + |y1-y2| )

![image](https://user-images.githubusercontent.com/45223821/110153821-e291e000-7e26-11eb-889d-f038360c340a.png)

1. 왼쪽 숫자 (1 4 7)을 눌렀을 경우, 왼손 직전 위치를 갱신한다.

2. 오른쪽 숫자 (3 6 9)를 눌렀을 경우, 오른손 직전 위치를 갱신한다.

3. 아닐 경우 최단 거리를 구한다.

    3-1. 왼손 좌표를 이용해 눌러야 하는 값과의 최단 거리를 구한다.

    3-2. 오른손 좌표를 이용해 눌러야 하는 값과의 최단 거리를 구한다.

    3-3. 왼손과 오른손의 최단 거리를 비교한다.

    3-4. 더 작은 경우를 직전 위치로 갱신한다.

        3-4-1. 만약 최단거리가 같다면, 매개변수 hand(왼/오른 손잡이)로 판단한다.

```java
import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        for(int i=0; i<numbers.length; i++) {
        	if(numbers[i]==0) {
        		numbers[i]=11;
        	}
        }
        
        int pre_l = 10; //직전 위치
        int pre_r = 12; //직전 위치
        int abs_r, abs_l;
        for(int i=0; i<numbers.length; i++) {
        	int num = numbers[i];
        	
        	if(num==1 || num==4 || num==7|| num==10) { // 왼쪽
        		answer += "L";
        		pre_l =num; //왼손 직전위치 갱신
        		continue;
        	} else if( num%3==0 ) { //오른쪽
        		answer += "R";
        		pre_r = num; //오른손 직전위치 갱신
        		continue;
        	} else {
        		int center = num/3; // 센터 x좌표

        		// 왼손 좌표값 맨해튼 거리
        		if(pre_l==1||pre_l==4||pre_l==7||pre_l==10) abs_l = Math.abs( (pre_l/3) -center)+1;
        		else abs_l=Math.abs( (pre_l/3) -center);
        		
        		// 오른손 좌표값 맨해튼 거리
        		if(pre_r%3==0) abs_r = Math.abs( (pre_r/3-1) -center)+1;
        		else abs_r = Math.abs( (pre_r/3) -center);
        		
                // 왼손 오른손 맨해튼 거리 비교
        		if(abs_l>abs_r) {
        			answer += "R";
        			pre_r = num;
        		} else if(abs_r>abs_l) {
        			answer += "L";
        			pre_l = num;
        		} else {
        	        if(hand.equals("right")) {
        	        	answer+="R";
        	        	pre_r=num;
        	        }
        	        else {
        	        	answer += "L";
            			pre_l = num;
        	        }
        		}
        	}
        }
        
        return answer;
    }
}
```


※ 좌표 구하는 방법

1. Left

   - x좌표 : 숫자/3

   - y좌표: 0

​

2. Center

   - x좌표: 숫자/3

   - y좌표: 1

​

3. Right

   - x좌표: 숫자/3

   - y좌표: 2

​

※ 최단 거리 구하는 방법

   1. 손의 직전 위치가 Left 혹은 Rigth일 때 
      - Left와 Right의 y좌표는 각각 0, 2이고, Center의 y좌표는 1이다. |x1-x2| + |y1-y2| 맨해튼 공식으로 구했을 때, 무조건 y좌표는 1이 나온다.

 

2. 손의 직전 위치가 Center일 때

    - Center의 y좌표는 1이니까 결과값의 y좌표는 무조건 0이 나옴


## 다른 풀이
- 이중좌표를 이용해, 최단 거리도 바로 대입해서 구함

```java
class Solution {
    //        0부터 9까지 좌표 {y,x}
    int[][] numpadPos = {
            {3,1}, //0
            {0,0}, //1
            {0,1}, //2
            {0,2}, //3
            {1,0}, //4
            {1,1}, //5
            {1,2}, //6
            {2,0}, //7
            {2,1}, //8
            {2,2}  //9
    };
    //초기 위치
    int[] leftPos = {3,0};
    int[] rightPos = {3,2};
    String hand;
    public String solution(int[] numbers, String hand) {
        this.hand = (hand.equals("right")) ? "R" : "L";

        String answer = "";
        for (int num : numbers) {
            String Umji = pushNumber(num);
            answer += Umji;

            if(Umji.equals("L")) {leftPos = numpadPos[num]; continue;}
            if(Umji.equals("R")) {rightPos = numpadPos[num]; continue;}
        }
        return answer;
    }

    //num버튼을 누를 때 어디 손을 사용하는가
    private String pushNumber(int num) {
        if(num==1 || num==4 || num==7) return "L";
        if(num==3 || num==6 || num==9) return "R";

        // 2,5,8,0 일때 어디 손가락이 가까운가
        if(getDist(leftPos, num) > getDist(rightPos, num)) return "R";
        if(getDist(leftPos, num) < getDist(rightPos, num)) return "L";

        //같으면 손잡이
        return this.hand;
    }

    //해당 위치와 번호 위치의 거리
    private int getDist(int[] pos, int num) {
        return Math.abs(pos[0]-numpadPos[num][0]) + Math.abs(pos[1]-numpadPos[num][1]);
    }
}

```


## 삽질
## 1. String "+"연산 사용

통과는 했지만 시간초과 말도안되게 차이난다

```java
    import java.util.*;

    class Solution {
        public String solution(int[] numbers, String hand) {
            String answer = "";
            
            for(int i=0; i<numbers.length; i++) {
                if(numbers[i]==0) {
                    numbers[i]=11;
                }
            }
            
            int pre_l = 10; //직전 위치
            int pre_r = 12; //직전 위치
            
            for(int i=0; i<numbers.length; i++) {
                int num = numbers[i];
                
                if(num==1 || num==4 || num==7|| num==10) { // 왼쪽
                    answer += "L";
                    pre_l =num; //왼손 직전위치 갱신
                    continue;
                } else if( num%3==0 ) { //오른쪽
                    answer += "R";
                    pre_r = num; //오른손 직전위치 갱신
                    continue;
                } else if(num==2 || num==5 || num==8 || num==11) {
                    int center = num/3; // 센터 x좌표

                    // 왼손 좌표값 맨해튼 거리
                    int abs_l = Math.abs( (pre_l/3) -center);
                    // 오른손 좌표값 맨해튼 거리
                    int abs_r = Math.abs( (pre_r/3-1) -center);
                    
                    if(abs_l>abs_r) {
                        answer += "R";
                        pre_r = num;
                    } else if(abs_r>abs_l) {
                        answer += "L";
                        pre_l = num;
                    } else {
                        if(hand.equals("right")) {
                            answer+="R";
                            pre_r=num;
                        }
                        else {
                            answer += "L";
                            pre_l = num;
                        }
                    }
                }
            }
            
            return answer;
        }
    }
```

1-1. String 연산 사용
    ![image](https://user-images.githubusercontent.com/45223821/110154223-58964700-7e27-11eb-8bb6-0c58e304c02e.png)



1-2. String Builder사용

![image](https://user-images.githubusercontent.com/45223821/110154865-21746580-7e28-11eb-9040-f19c105de484.png)




## 2. 초기 풀이

정확성 : 60

이건 키패드의 버튼을 눌렀을 때 경우의 수를 생각해봐서 대입한 풀이다.코드가 좀 더럽긴한데.. 솔직히 반례를 못찾겠다 ㅋㅋㅋㅋ

​

   1. 왼쪽일 떄

   2. 오른쪽일 때

   3. 가운데일 때

      3-1. 최단거리를 가중치로 생각하고, 직전 위치와 현재 위치의 차를 구해 가중치로 대소 비교한다.

​

<경우의 수> 

   1.  1 4 7 : 왼쪽일 떄

   2.  3 6 9 : 오른쪽일 때

   3.  2 5 8 11 : 가운데일 때

        - 가중치가 1일 떄

            양옆에 +1or 위아래 +3

        - 가중치가 2일 떄

            2 or  4 or 6차이

        - 가중치가 3일 떄

            5 or 7

       - 가중치가 4일 떄

            8 or 10차이
```java
import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        for(int i=0; i<numbers.length; i++) {
        	if(numbers[i]==0) {
        		numbers[i]=11;
        	}
        }
        
        int pre_l = 10; //직전 위치
        int pre_r = 12; //직전 위치
        
         for(int i=0; i<numbers.length; i++) {
        	int num = numbers[i];
        	
        	if(num==1 || num==4 || num==7|| num==10) { // 왼쪽
        		answer += "L";
        		pre_l =num;
        		continue;
        	} else if( num%3==0 ) { //오른쪽
        		answer += "R";
        		pre_r = num;
        		continue;
        	} else if(num==2 || num==5 || num==8 || num==11) {
        		int abs_r = Math.abs(num-pre_r);
        		int abs_l = Math.abs(num-pre_l);
        		
        		// 오른손 가중치 검사 
        		if(abs_r==1 || abs_r==3) { // 가중치가 1일 때 
        			abs_r=1;
        		} else if(abs_r==2|| abs_r==4|| abs_r==6) {
        			abs_r=2;
        		} else if(abs_r==5|| abs_r==7) {
        			abs_r=3;
        		} else if(abs_r==8|| abs_r==10){
        			abs_r = 4;
        		}
        		
        		// 왼손 가중치 검사 
        		if(abs_l==1 || abs_l==3) {
        			abs_l = 1;
        		} else if(abs_l==2|| abs_l==4) {
        			abs_l = 2;
        		} else if(abs_l==5|| abs_l==7|| abs_l==6) {
        			abs_l = 3;
        		} else if(abs_l==8|| abs_l==10){
        			abs_l = 4;
        		} 
        		
        		// 오른손 , 왼손 비교 
        		if(abs_l > abs_r) {
        			pre_r =num;
        			answer += "R";
        		} else if(abs_l < abs_r) {
        			pre_l =num;
        			answer += "L";
        		} else {
        			 if(hand.equals("right")) {
         	        	answer+="R";
         	        	pre_r=num;
         	        }
         	        else {
         	        	answer += "L";
             			pre_l = num;
         	        }
        		}
        	}
        }
        
        return answer;
    }
}
```

## Ref
1. 맨해튼 거리

    https://rebro.kr/60

​

2. String + 연산 동작 방식

    https://codingdog.tistory.com/entry/java-string-%EC%97%B0%EC%82%B0-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91%ED%95%98%EB%8A%94%EC%A7%80-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4