## 2주차 2

**문제1**

### 정수 내림차순으로 배치하기

https://programmers.co.kr/learn/courses/30/lessons/12933
```java

import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String str =String.valueOf(n);
        
        char[] ch =str.toCharArray();
        
        Arrays.sort(ch);
        
        str= "";
        
        for(int i =ch.length-1;i>=0;i--) {
            str+=ch[i];
        }
        answer = Long.parseLong(str);
        return answer;
    }
}
```

## 풀이 
* 스트링변수에 String.valueOf로 n값을 문자열로 저장,  toCharArray를 이용 문자열을 char형 배열에 담아줌 
* Arrays.sort로 배열 오름차순 정렬, 배열의 역순으로 for문 돌려 저장 
정수형long 으로 변환  answer에 저장
   
**문제2**

### 짝수와 홀수

https://programmers.co.kr/learn/courses/30/lessons/12937
```java
class Solution {
    public String solution(int num) {
       
        return num%2 ==0 ? "Even": "Odd";
    }
}

```

## 풀이
* 삼항연산자 이용 
  
**문제3**

### 핸드폰 번호 가리기

https://programmers.co.kr/learn/courses/30/lessons/12948

```java
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int pLength = phone_number.length();
        
        for(int i =0; i< pLength; i++) {
            if(i <pLength -4)
                answer += "*";
            else
                answer += phone_number.charAt(i);
        }
        return answer;
    }
}
```
## 풀이
*  문자열 길이 -4 번째 까지 *, 그외 핸드폰 번호 출력 

**문제4**

### 콜라츠 추측

https://programmers.co.kr/learn/courses/30/lessons/12943

class Solution {
    public int solution(int num) {
       
      
        
        int answer = 0;
        long num1 = num;
        for( int i =0; i< 500; i++) {
            if(num1 == 1) {
                break;
            }
            if (num1%2 ==0)
                num1 /=2;
            else
                num1 = num1*3 +1;
                
            answer++;
        }
        return answer < 500 ? answer : -1;
    }
}

# 질문
* 실행하는데 자꾸 2개씩 실패떠서  long형 변수에 담아서 실행하니 성공하네요
 크기문제일까요 아시는분 답변 부탁드립니다.
**문제5**

### x만큼 간격이 있는 n개의 숫자

https://programmers.co.kr/learn/courses/30/lessons/12954
```java
class Solution {
    public long[] solution(int x, int n) {
        long x1 = x;
        long[] answer = new long[n];
        
        for(int i=0; i<n; i++){
            answer[i] = x1*(i+1);
        }
        return answer;
    }
}
```

 