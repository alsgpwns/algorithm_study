# Day4 [Level1]
### 문제1
![문1](https://user-images.githubusercontent.com/45223821/105829931-447d4f80-6008-11eb-959d-40c99109b105.PNG)
<https://programmers.co.kr/learn/courses/30/lessons/12912>

### 문제 설명
- 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
- 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

### 입출력 예
![1입출](https://user-images.githubusercontent.com/45223821/105829993-5232d500-6008-11eb-830c-54490f14bc44.PNG)

### 풀이
- a,b는 아래와 같은 세가지 상태로 구분된다.
- (1) a>b　(2)a<b　(3) a=b
  1. (1) 혹은 (2) 일 때, 작은 수 부터 큰 수 까지의 합을 구하면 되는 문제이다. 때문에 Math.min함수와 Math.max 함수를 사용하여 구간의 합을 return한다.
  2. (3) a==b 일 때, a와b가 동일하기 때문에, a혹은 b를 return한다. 
```java
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if(a==b) return a;
        else {
        	for(int i=Math.min(a, b); i<=Math.max(a, b); i++) answer+=i;
        }
        return answer;
    }
}
```
### 시간 복잡도
- O(n)

### Ref
1. (Math.max, Math.min) https://www.geeksforgeeks.org/java-math-max-method-examples/   
   

---
   

### 문제2
![문2](https://user-images.githubusercontent.com/45223821/105829942-46471300-6008-11eb-8fd9-e93dd85ebed1.PNG)
<https://programmers.co.kr/learn/courses/30/lessons/12916>

### 문제 설명
- 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
- 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
- 예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

### 입출력 예
![입2](https://user-images.githubusercontent.com/45223821/105829990-519a3e80-6008-11eb-98fb-d75edb963610.PNG)

### 풀이
1. 반복문으로 String 문자열의 길이만큼 반복한다.
2. charAt메소드를 이용해 비교한다.
   -  y 혹은 Y일 때, Y의 갯수를 셀 변수를 1증가 시킨다.
   -  p 혹은 p일 때, P의 갯수를 셀 변수를 1증가 시킨다.
3. y의 갯수와 p의 갯수를 비교하여, 다르면 false, 같으면 true를 return한다.
```java
class Solution{
    boolean solution(String s) {
        boolean answer = true;
        int yNum=0, pNum=0;
        for(int i=0;i<s.length();i++)
        {
        	if(s.charAt(i)=='y'||s.charAt(i)=='Y') yNum++;
        	else if(s.charAt(i)=='p'||s.charAt(i)=='P') pNum++;
        }
        if(yNum!=pNum) return false;

        return answer;
    }
}
```

### 시간 복잡도
- O(n)
  
### Ref
1. (charAt) https://www.w3schools.com/java/ref_string_charat.asp
2. (charAt) https://blog.naver.com/5550304/222171205425