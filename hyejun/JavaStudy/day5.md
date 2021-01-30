# Day4 [Level1]
### 문제1
!![image](https://user-images.githubusercontent.com/45223821/106151525-c794d600-61bf-11eb-8f10-bf2326a31b4e.png)
   
<https://programmers.co.kr/learn/courses/30/lessons/12915?language=java>

### 문제 설명
- 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106151695-f7dc7480-61bf-11eb-8032-ed55ed40b01e.png)

### 풀이
1. n번째 문자를 문자열 앞에 붙여, n번째 문자로 비교하며 sort한다.
   - n번째 문자를 추출하기 위해 charAt 메소드를 사용했다.

2. sort후 앞에 붙인 n번째 문자열을 제거한다.
   - indexOf를 사용하여, 특수 문자를 ("/") 체크한다.
   - subString을 사용하여 문자열을 자른다.

```java
import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
       String[] answer = new String[strings.length];
        
        for(int i=0; i<strings.length; i++) {
        	char temp=strings[i].charAt(n);
        	answer[i]=strings[i].valueOf(temp)+"/"+strings[i];
        }
        
        Arrays.sort(answer);
        
        for(int i=0; i<answer.length; i++) {
        	answer[i]=answer[i].substring(answer[i].indexOf("/")+1);
        }
        return answer;
    }
}
```

### 다른 풀이
```java
import java.util.*;

class Solution {
  public String[] solution(String[] strings, int n) {
      Arrays.sort(strings, new Comparator<String>(){
          @Override
          public int compare(String s1, String s2){
              if(s1.charAt(n) > s2.charAt(n)) return 1;
              else if(s1.charAt(n) == s2.charAt(n)) return s1.compareTo(s2);
              else if(s1.charAt(n) < s2.charAt(n)) return -1;
              else return 0;
          }
      });
      return strings;
  }
}
```

---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106151912-36722f00-61c0-11eb-8250-052de686428a.png)
   
<https://programmers.co.kr/learn/courses/30/lessons/12915>

### 문제 설명
- 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106152103-66b9cd80-61c0-11eb-8217-a157dcdab05c.png)

### 풀이

간단하다.

1. arr 배열의 원소를 divisor로 나누었을 떄, 나누어 떨어진다면 answer에 add한다.

2. 나누어 떨어진것이 없다면, answer의 size는 0이라고 판단하고, return -1을 해준다.

```java
import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
       String[] answer = new String[strings.length];
        
        for(int i=0; i<strings.length; i++) {
        	char temp=strings[i].charAt(n);
        	answer[i]=strings[i].valueOf(temp)+"/"+strings[i];
        }
        
        Arrays.sort(answer);
        
        for(int i=0; i<answer.length; i++) {
        	answer[i]=answer[i].substring(answer[i].indexOf("/")+1);
        }
        return answer;
    }
}
```

---
### 문제3
![image](https://user-images.githubusercontent.com/45223821/106152178-7c2ef780-61c0-11eb-9195-8dde4d7e1d58.png)

<https://programmers.co.kr/learn/courses/30/lessons/12917>

### 문제
- 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
- 문제 그대로, 문자열을 내림차순으로 배열해주면된다.
   

### 풀이
- 간단하다.
1. 문자열 sort
2. sort된 문자열을 역순으로 answer에 담아준다.

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
#### 블로그
<https://blog.naver.com/5550304/222223583151>