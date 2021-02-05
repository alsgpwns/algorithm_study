# Day10 [Level]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/106856671-30210d00-6702-11eb-8187-32d80747f2fc.png)


<https://programmers.co.kr/learn/courses/30/lessons/12947>

### 문제 설명
자연수 x를 입력받아 x가 하샤드 수 인지 검사한다.

자연수 x의 일의 자리부터 n의 자리까지 더해, 본래의 값이 더한값으로 나누어 떨어진다면 하샤드 수이다.

ex) 10

1+0 => 1

10/1 => 나누어 떨어지므로 하샤드수

### 풀이
1. 매개변수 x를 받아 while문을 돌며 x를 일의자리부터 n의 자리까지 더해, 변수 sum에 담는다

2. 매개변수 x(변수 temp)를 sum으로 나누어떨어진다면 true, 아니라면 false를 반환한다.
```java
class Solution {
    public boolean solution(int x) {
        int sum=0;
        int temp=x;

        while(x>0) {
			sum += x%10;
			x=x/10;
		}
        return (temp%sum==0)? true: false;
    }
}
```
### 다른 풀이
1. split와 String.valueOf메소드를 이용해, String 배열 초기화

2. 변수 sum에 s를 더해준다

3. x가 sum으로 나누어 떨어진다면 true 반환, 아니라면 false반환
```java
class Solution {
    public boolean solution(int x) {
        String[] temp = String.valueOf(x).split("");
		int sum = 0;
		for (String s : temp) {
			sum += Integer.parseInt(s);
		}
		
		return (x%sum==0)? true: false;
    }
}
```
---
### 문제2


<https://programmers.co.kr/learn/courses/30/lessons/12969>

### 문제 설명
입력받은 가로, 세로의 길이로 직사각형 형태의 별찍기를 해준다.


### 풀이
간단하다.

별의 세로 갯수는 이중 FOR문의 밖,가로 갯수는 이중 FOR문의 안으로 찍어주면 된다.
```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

         for(int i=0; i<b; i++) {
        	for(int j=0; j<a; j++) {
        		System.out.print("*");
        	}
        	System.out.println();
        }
    }
}
```

---
### 문제3
<https://programmers.co.kr/learn/courses/30/lessons/12934>

### 문제 설명
문제 이름 그대로, 매개변수 n의 정수 제곱근을 판단한다.

ex) 121 -> 11의 제곱근 이므로, n+1의 제곱근을 return

ex) 3 -> 1.xxxx의 제곱근 이므로, -1을 return


### 풀이
1. Math.sqrt메소드를 이용해, 매개변수 n의 제곱근을 구한다.

2. 제곱근이 정수인지 판단하기 위해, dobule type의 제곱근과 int type의 제곱근을 비교한다.

    ( 3 -> double: 1.xxxx / int : 1 )

3. int 제곱근과 double 제곱근이 같다면, n+1의 제곱근을 return, 다르다면, -1을 return
```java
import java.util.*;
class Solution {
    public long solution(long n) {
        double result = Math.sqrt(n);      
        return (long) (((int)result==result)? (result+1)*(result+1): -1);
    }
}
```
### 다른 풀이
- 로직이 같은 풀이
    ```java
    class Solution {
    public long solution(long n) {
        if (Math.pow((int)Math.sqrt(n), 2) == n) {
                return (long) Math.pow(Math.sqrt(n) + 1, 2);
            }
            return -1;
    }
    }
    ```
- Math.floor를 이용한 풀이

    나는 type변환을 이용했는데, 이 풀이는 floor(버림)을 이용해서 풀었다.
    ```java
    class Solution {
    public long solution(long n) {

        double i = Math.sqrt(n);

        return Math.floor(i) == i ? (long) Math.pow(i + 1, 2) : -1;
    }
    }
    ```

---
### 문제4 [In progress]
최대공약수와 최소공배수

### 문제 설명
매개변수의 최대공약수와 최소 공배수를 구해서 return

### 풀이
- 우선 구현해보고 리팩토링 할 예정
```java
import java.util.*;
class Solution {
    public int[] solution(int n, int m) {
       int[] answer = {1,1};
        ArrayList <Integer> min = new ArrayList<Integer>(); //최소공배수
        ArrayList <Integer> max_n = new ArrayList<Integer>(); //최대공약수
        ArrayList <Integer> max_m = new ArrayList<Integer>(); //최대공약수      
        int a=n;
        int b=m;
         //최소공배수
        while(n>=1) {
        	if(n%2==0 && m%2==0) {
        		n=n/2;
        		m=m/2;
        		min.add(2);
        		min.add(n);
        		min.add(m);
        	}
        	else if(n%3==0 && m%3==0) {
        		n=n/3;
        		m=m/3;
        		min.add(3);
        		min.add(n);
        		min.add(m);
        	}
        	else break;
        }
        if(min.size()==0) {
        	min.add(n);
        	min.add(m);
        }
        for(int i=0; i<min.size(); i++) {
        	answer[1]=answer[1]*min.get(i);
        }
        
        //최대 공약수
        while(a>=1 && b>=1) {
        	max_n.add(a);
        	max_m.add(b);
        	if(a%2==0) a=a/2;
        	else if(a%3==0) a=a/3;
        	if(b%2==0) b=b/2;
        	else if(b%3==0) b=b/3;
        	else break;
        }
         if(min.size()==2) {
        	answer[0]=1;
        }
        else
        for(int i=0; i<max_n.size()-1; i++) {
        	if( max_m.contains(max_n.get(i)) ) answer[0]=answer[0]*max_n.get(i);
        }
         return answer;
    }
}
```

---
### 문제5 [In progress]
2016 

