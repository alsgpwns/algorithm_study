# Day7 [Level1]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/106389347-33787800-6426-11eb-800d-c6de9fa7fe10.png)
- <https://programmers.co.kr/learn/courses/30/lessons/12926>
- 유형: 문자열, 아스키코드

### 문제 설명
매개변수로 문자열s, 정수 n을 받는다.


s를 n만큼 더해준 '시저 암호'를 만드는 문제이다.


이를 위해 아스키코드를 사용했다.


### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106389351-35dad200-6426-11eb-9fbc-b62f46443fc2.png)

### 풀이
- 매개변수로 받은 s의 상태는 아래와 같이 두개로 나뉜다.

1. null (공백) 일 때

2. 소문자 or 대문자 일 때

​

- 더한 후 문자의 상태

1. null (공백은 어떤 숫자를 더해도 공백이다.)

2. 더한 후 소문자or대문자의 범위를 넘어갈 떄 ( z+1 = a)

3. 더한 후 일반적인 상태일 때 ( AB+1 = BC)

​

- 생각한 알고리즘

1. null 일 떄
    - answer에 null을 넣어준다.

​

1. 더한 후 범위를 넘어갈 때

    - 더한 후 범위를 넘어가도, 다시 a로 돌아올 수 있도록, 아스키코드로 -26을 해준다.

​

3. 더한 후 일반적인 상태일 때

    - +n (그냥 더해준다)



```java
class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++) {	
			char ch=s.charAt(i);
			if(ch==' ') {  /*첫번째 상태*/
				answer+=(char)ch;
			} else if('a'<=ch && ch<='z' && ch+n>'z' || 'A'<=ch && ch<='Z' && ch+n >'Z') {  /*두번째 상태*/
				int ask= (ch+n-26);
				answer+=(char)ask;
			}  else {  /*세번째 상태*/
				int ask=ch+n;
				answer+=(char)ask;
			}
			
		}
        return answer;
    }
}

```

[10진수 → 아스키코드 ]

아스키코드로 변환후, 숫자가 출력돼서 당황했는데,

char형으로 변환해주면, 문자가 출력된다.
  ```java
  char ch=s.charAt(i);
answer+=(char)ask;
  ```

  ※ 아스키코드를 사용한 비슷한 문제

<https://blog.naver.com/5550304/222043306872>
### 다른 풀이
```java
class Solution {
	public String solution(String s, int n) {
		String answer = "";
		n = n % 26;
		for (int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			if (Character.isLowerCase(ch)) {
				ch = (char) ((ch - 'a' + n) % 26 + 'a');
			} else if (Character.isUpperCase(ch)) {
				ch = (char) ((ch - 'A' + n) % 26 + 'A');
			}
			answer += ch;
		}
		System.out.println(answer);
		return answer;
	}
}
```

- isUpperCase()
    
    isUpperCase메소드를 이용해 받은 인자가 영문 대문자/소문자 여부를 판단해 true 혹은 false값을 리턴해준다.

```java
Character.isUpperCase(ch)
```

---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106389524-fb256980-6426-11eb-868c-f5f60e1562fe.png)

<https://programmers.co.kr/learn/courses/30/lessons/12935>

### 문제 설명
배열 arr에서 가장 작은 수를 제거한 배열 answer를 return한다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106389525-fd87c380-6426-11eb-87b2-dfe21b59aff5.png)

### 풀이
1. 이중 for문을 이용해 가장 작은 값 (min)을 찾는다.

2. arr의 요소(values)가 min과 같지 않다면, answer배열에 arr 요소(values)를 넣어준다.

3. answer배열 return

   - 문제 요구사항엔 배열이 빈 경우, 배열에 -1을 return하라고 명시되어있다. 하지만 테스트케이스엔 없는것같아 삭제했다. (근데 넣어야될것같다.)

```java
class Solution {
    public int[] solution(int[] arr) {
         int[] answer = new int[arr.length-1];
         int count=0;
        
        // min 찾기
        int min = arr[0];
        for(int i=0; i<arr.length-1; i++) {
        	for(int j=i+1; j<arr.length; j++) {
        		int temp = Math.min(arr[i], arr[j]);
        		if(min>temp) min=temp;
        	}
        }
        
        for(int i=0; i<arr.length; i++) {
        	if(! (arr[i]==min)) answer[count++]=arr[i];
        }
        
        return answer;
    }
}
```
### 다른 풀이
1. 비슷한 풀이

    - for문과 if문을 이용해 최소값 (minIndex)를 찾는다. 

        → index 번호

    - minIdex를 삭제하기 위해, minIdex보다 한칸 뒤의 Index부터 (minindex+1) arr에 넣어준다.
    
        → min값을 제거한 arr을 만듦


    - answer array에 min값을 제거한 arr을 넣어준다.
    
    ```java
    class Solution{
        public int[] solution(int[] arr) {
            /*첫번 째*/
            if (arr.length == 1) {
                arr[0] = -1;
                return arr;
            } 
            
            int[] answer = new int[arr.length-1];
            int minIndex=0;

            /*두번 째*/
            for(int i=0; i<arr.length; i++){
                if(arr[minIndex]>arr[i]){
                    minIndex = i;
                }
            }

            /*세번 째*/
            for(int i=minIndex+1; i<arr.length; i++){
                arr[i-1] = arr[i];
            }
            
            /*네번 째*/
            for(int i=0; i<answer.length; i++){
                answer[i] = arr[i];
            }
            
            
            return answer;
        }
    }
    ```
    - 나는 최소값을 이중for문으로 찾았는데, 아래와 같이 for문과 if문을 사용해 for문 하나로도 구현할 수 있다.
    ```java
            /*두번 째*/
            for(int i=0; i<arr.length; i++){
                if(arr[minIndex]>arr[i]){
                    minIndex = i;
                }
            }

    ```

2. ArrayList를 사용한 풀이
   - ArrayList를 생성한다.

   - 생성된 ArrayList에 arr배열의 값을 넣어준다.

   - Collections.min 메소드를 사용해, 가장 작은 값을 min 변수에 대입한다.

   - ArrayLisy.remove 메소드를 사용해, ArrayList에 저장되어있는 min(가장 작은 값)을 삭제한다.

   - ArrayList에 저장되어있는 값을 answer배열에 대입한다.

   - answer 배열 return
        ```java
        class Solution{
        public int[] solution(int[] arr) {
            int[] answer = new int[arr.length-1];
            
            if (arr.length == 1) {
                arr[0] = -1;
                return arr;
            } 
            
            ArrayList<Integer> list= new ArrayList<Integer>();
            for (int a : arr) {
                list.add(a);
            }
            
            Integer min= Collections.min(list);
            list.remove(min);

            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }
            
            return answer;
            }
        }
        ```
    - Collections.max() , Collections.min() 메소드

        지정된 컬렉션의 가장 큰 요소/ 가장 작은 요소를 반환한다.
        ```java
        Integer[] list = { 1123, 1412, 23, 44, 512132 };
        List<Integer> arr = new ArrayList<>(Arrays.asList(list));

        System.out.println(Collections.max(arr)); // 512132
        System.out.println(Collections.min(arr)); // 23
        ```

---
### 문제3
![image](https://user-images.githubusercontent.com/45223821/106389638-b9e18980-6427-11eb-948d-117ef45eecb2.png)

<https://programmers.co.kr/learn/courses/30/lessons/12931>

### 문제 설명
자연수 n의  각 자릿수의 합을 구해 return한다.

### 입출력 예

![image](https://user-images.githubusercontent.com/45223821/106389641-bd751080-6427-11eb-915f-ae170ffb6de6.png)

### 풀이
간단하다.

​
int n을 String형으로 형변환 해준 뒤,

charAt메소드를 이용해 모든 원소를 더해준다.

더한 값을 answer에 넣고, return한다.

```java
public class Solution {
    public int solution(int n) {
        int answer = 0;
        String str=Integer.toString(n);
       
       for(int i=0; i<str.length(); i++) {
    	   answer+=str.charAt(i)-48;
       }
        return answer;
    }
}
```
### 다른 풀이

- 타입변환 없이 풀 수 있는 코드

  1. n%10을 이용해, 일의 자리부터 구해서, answer에 더해준다.

  2. n/ 10을 이용해, n의 자리수를 하나씩 감소시킨다.

    ```java
    public class Solution {
        public int solution(int n) {
            int answer = 0;
            while(n>0){
                answer+=n%10;
                n=n/10;
            }
            return answer;
        }
    }
    ```

