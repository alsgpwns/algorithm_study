# 2주차 3 

**문제1** 

### 하샤드 수

https://programmers.co.kr/learn/courses/30/lessons/12947

```java
class Solution {
    public boolean solution(int x) {
        boolean answer ;
        
        int sum =0;
        int x1 =x;
        while(x>0) {
            sum += x%10;
            x = x/10;
        }
        
        if(x1%sum == 0 ){
            answer = true;
            
        }else{
            answer =false;
        }
        return answer;
    }
}
```
**문제2**

### 2016년

https://programmers.co.kr/learn/courses/30/lessons/12901

```java
class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int[] days = {31,29,31,30,31,30,31,31,30,31,30,31};
        
        int day = 0;
        for( int i =0; i<a-1; i++) {
            day += days[i];
        } 
        
        day +=b;
        day = day %7;
        
          switch(day){
            case 1 :
                answer += "FRI";
                break;
            case 2 :
                answer += "SAT";
                break;
            case 3 : 
                answer += "SUN";
                break;
            case 4 : 
                answer += "MON";
                break;
            case 5 : 
                answer += "TUE";
                break;
            case 6 : 
                answer += "WED";
                break;
            case 0 : 
                answer += "THU";
                break;
        }
        return answer;
    }
}
```

**문제3**

### 직사각형 별 찍기

https://programmers.co.kr/learn/courses/30/lessons/12969
```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        
        for(int i =0; i<b; i++){
            
             for(int j=0; j<a; j++) {
                 System.out.print("*");
             }
             System.out.println("");
        }
    
    }
}
```

**문제4**

### 정수 제곱근 판별 
```java
https://programmers.co.kr/learn/courses/30/lessons/12934

class Solution {
    public long solution(long n) {
        long answer = -1;
   
       double num = Math.sqrt(n);
        
        if(num %1 == 0) {
            num++;
       
                answer = (long) (num*num);
        }
        
        return answer;
    }
}
```

**문제5**

### 최대공약수와 최소 공배수

https://programmers.co.kr/learn/courses/30/lessons/12940
```java
class Solution {
    public int[] solution(int n, int m) {
        int gcd = GCD(n, m);
        int lcm = LCM(n, m, gcd);
        int[] answer = {gcd, lcm};
        return answer;
    }

    public int GCD(int n, int m){
        if(m > n){
            int temp = n;
            n = m;
            m = temp;
        }
        while(m != 0){
            int temp = n % m;
            n = m;
            m = temp;
        }
        return n;
    }
    public int LCM(int n, int m, int gcd){
        int result = (n / gcd) * (m / gcd) * gcd;
        return result;
    }
}
```