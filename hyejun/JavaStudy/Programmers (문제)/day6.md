# Day9 [Level]
### 문제1

![image](https://user-images.githubusercontent.com/45223821/106855580-7d9c7a80-6700-11eb-9b3c-f3fa2fa1248a.png)

<https://programmers.co.kr/learn/courses/30/lessons/12933?language=java>

### 문제 설명
long 형으로 받은 정수 n을 내림차순으로 정렬하여 return한다.

### 풀이
1. long → String 형변환하여 변수에 담아준다.

2. Stirng 변수에서 한 문자씩 읽어와 (charAt) int 배열에 넣어준다.

3. int 배열을 오름차순 sort후, 역순으로 읽어와 String변수에 대입한다.

4. String 변수를 long형으로 형변환 후, return해준다.
   

```java
import java.util.*;
class Solution {
    public long solution(long n) {
        long answer=0;

        /*첫번째*/
        String str = Long.toString(n);
        String num_str="";
        int[] arr=new int[str.length()];

        /*두번째*/
        for(int i=0; i<str.length(); i++) {
             arr[i]=str.charAt(i)-'0';
        }

        /*세번째*/
        Arrays.sort(arr);
        for(int i=str.length()-1; i>=0; i--) {
            num_str += arr[i];
        }

        /*네번째*/
        answer = Long.parseLong(num_str);
        return answer;
    }
}
```
※ String -> Long 형변환 메소드

Integer.parseInt()를 사용했었는데, 계속 런타임 에러가 났었다.
```java
    Long.parseLong(num_str);
```

### 다른 풀이
로직은 나와 같은데, split로 배열을 초기화 해서 훨씬 코드가 간결하고 가독성이 좋다.
```java
import java.util.*;
class Solution {
    public long solution(long n) {
        String arr[]=String.valueOf(n).split("");
        Arrays.sort(arr);
        String str = "";
        for(int i=arr.length-1; i>=0; i--){
             str+= arr[i];
        }
        return Long.parseLong(str);
    }
}
```
- split를 사용하여 String 배열을 초기화 하는 방법
```java
String arr[]=String.valueOf(n).split("");
```


---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106855837-f00d5a80-6700-11eb-9910-cdf81533950a.png)


<https://programmers.co.kr/learn/courses/30/lessons/12937>

### 문제 설명
num이 홀수이면 Odd를 반환,

num이 짝수이면 Even을 반환한다.


### 풀이
아주 간단하다. 문제와 같음
```java
class Solution {
    public String solution(int num) {
        String answer = "";
        if(num%2!=0) answer="Odd";
        else answer="Even";
        return answer;
    }
}
```
삼항연산자를 이용해 풀 수 있다.
```java
class Solution {
    public String solution(int num) {
        return num % 2 == 0 ? "Even": "Odd";
    }
}
```
---
### 문제3
![image](https://user-images.githubusercontent.com/45223821/106855945-1632fa80-6701-11eb-94c9-e179af1525b0.png)


<https://programmers.co.kr/learn/courses/30/lessons/12943>

### 문제 설명
1. 입력된 수가 짝수라면, 2로 나눈다.

    1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.

2. 결과로 나온 수에 같은 작업을 1이 될 때 까지 반복한다.

※ 작업을 500번 반복해도 1이 되지 않는다면, -1을 반환한다.


### 풀이
문제에 나온 설명과 같이 풀면된다.

하지만, 입력받은 매개변수 타입(int로) 500번 이상 연산을 하면, overflow가 발생한다.

(매개변수로 626331을 받았을 때, 488번 만에 1이 된다.)

때문에 매개변수 type을 long형으로 변환해주면 돌아간다.
```java
class Solution {
    public int solution(int num) {
        int answer = 0;
        long number = num;
        while(number!=1 && answer<=500) {
        	number= (number%2 == 0) ? (number/2) : (number*3+1);
        	answer++;
        }
        if (answer>=500) return -1;
        return answer;
    }
}

```

### 다른 풀이
```java
class Solution {
    public int solution(int num) {
        int answer = 0;
        long number = num;
        while(num!=1 && answer!=500) {
        	if(number%2==0) number=number/2;
        	else number=(number*3)+1;
        	answer++;
        }
        if(answer>=500) return -1;
        return answer;
    }
}

```


---
### 문제4
![image](https://user-images.githubusercontent.com/45223821/106856035-411d4e80-6701-11eb-9695-37741617ab58.png)


<https://programmers.co.kr/learn/courses/30/lessons/12948>


### 문제 설명
문자열 s의 마지막 4자리를 "*"로 변경하여, 문자열을 return해준다.

### 풀이
StringBuilder의 SetCharAt을 이용해 풀었다.

for문으로 0 ~ phone_number길이-4 까지 *로 변환해준다.

변환해준 값을 String형으로 return해준다.
```java
class Solution {
    public String solution(String phone_number) {
        String answer = "";
         StringBuilder builder = new StringBuilder(phone_number);
		 for(int i=0; i<phone_number.length()-4; i++) {
			 builder.setCharAt(i, '*');
		 }
		 answer = builder.toString();
        return answer;
    }
}
```
※ StringBuilder 기본 사용법
```java
StringBuilder builder = enw StringBuilder(문자열);
builder.setCharAr(index,char);
```

### 다른 풀이
- 로직이 같은 풀이
    ```java
    class Solution {
    public String solution(String phone_number) {
        char[] ch = phone_number.toCharArray();
        for(int i = 0; i < ch.length - 4; i ++){
            ch[i] = '*';
        }
        return String.valueOf(ch);
    }
    }
    ```
    ※ toCharArray 기본 사용법
    toCharArray메소드는 문자열을 char형 배열로 바꾼다.
    ```java
    public char[] toCharArray()
    char[] arr =문자열.toCharArray();
    ```

- substring을 사용한 풀이

    1. "*"을 0~phone_number길이-4 까지 채운다.

    2. 1을 answer변수에 대입

    3. answer에 phone_number의 마지막 4를 잘라 붙여준다.
    ```java
    class Solution {
    public String solution(String phone_number) {
        String answer = "";
            for (int i = 0; i < phone_number.length() - 4; i++)
                answer += "*";
            answer += phone_number.substring(phone_number.length() - 4);
            return answer;
        }
    }
    ```

---
### 문제5
![image](https://user-images.githubusercontent.com/45223821/106856333-a4a77c00-6701-11eb-98cc-bc553259be13.png)


<https://programmers.co.kr/learn/courses/30/lessons/12954>

### 문제 설명
정수 x와 자연수 n을 입력받아, x부터 x씩 증가하는 숫자를 n개 지니는 리스트를 return한다.


### 풀이
간단하다. 문제 설명과 같이 풀면된다.

이 문제에서도 주의할 점은 최대 값, 최소 값을 계산했을 떄 overflow가 발생한다는 점이다.

떄문에 int 형을 long형으로 변환한다.
```java
class Solution {
    public long[] solution(int x, int n) {
       long[] answer = new long[(int)n];
        long num=x;
        for(int i=0; i<n; i++){
            answer[i] = num*(i+1);
        }
        return answer;
    }
}
```

※ int 형 범위
-2,147,483,648 ~ 2,147,483,647 이다.

### 다른 풀이
1. Long.valueOf를 이용한 풀이
    ```java
    class Solution {
    public long[] solution(int x, int n) {
            long[] answer = null;
            answer = new long[n];
            for(int i=0;i<n;i++){
                answer[i]=Long.valueOf(x)*(i+1);
            }
            return answer;
    }
    }
    ```
    Long.valueOf 메소드를 이용해, Long객체 반환한다.

    (이 메소드를 사용하면, long변수를 따로 초기화 해주지 않아도된다.)
    ```java
    Long.valueOf(x)
    ```
2. 직전 Index 값에 x를 더하는 방식으로도 풀 수 있다.
    ```java
    class Solution {
        public static long[] solution(int x, int n) {
            long[] answer = new long[n];
            answer[0] = x;
            for (int i = 1; i < n; i++) {
                answer[i] = answer[i - 1] + x;
            }
            return answer;

        }
    }
    ```
### 메소드 Ref
<https://studymake.tistory.com/421>