# Day12 [Hash]
### 문제1
https://programmers.co.kr/learn/courses/30/lessons/42577

### 문제 설명
String 배열의 원소 중 하나가 다른 원소의 접두사 일 때 false를 반환, 아닐 때 true를 반환한다.

### 풀이
1. SubString 메소드를 이용한 풀이 (처음 풀이)

   - 이중 for문으로 비교할 대상 i와 체크할 대상 j를 정한다.

   - i를 prefix(접두사)로 생각하고, 변수에 대입한다.

   - [i]와 [j]를 비교해, 더 긴 길이의 배열을 짧은 배열로 자른 후, 긴 문자열이 짧은 문자열로 시작하는지 비교한다.

       - 만약 3번 조건이 충족한다면, false를 return 해준다.


    ```java
    import java.util.*;
    class Solution {
        public boolean solution(String[] phone_book) {
        boolean answer = true;
            Arrays.sort(phone_book);
            
            for(int i=0; i<phone_book.length-1; i++) {
                String prefix = phone_book[i];
                for(int j=i+1; j<phone_book.length; j++) {
                    if(prefix.length()<=phone_book[j].length()) {
                        String temp = phone_book[j].substring(0, prefix.length());
                        if(prefix.equals(temp)) return false;
                    }
                    else break;
                }
            }
            return answer;
        }
    }
    ```


2. startsWith 메소드를 활용한 풀이 (개선한 풀이)
   - 이중 for문으로 비교할 대상 i와 체크할 대상 j를 정한다.

   - i를 prefix(접두사)로 생각하고, 변수에 대입한다.

   - startsWith 메소드를 이용해, [i]혹은 [j] 문자열이 접두사인지 비교한다.
```java
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
       	boolean answer = true;
        
		for(int i=0; i<phone_book.length-1; i++)
		{
			String prefix = phone_book[i];
			for(int j=i+1; j<phone_book.length; j++)
			{
				if(prefix.startsWith(phone_book[j])) return false;
				if(phone_book[j].startsWith(prefix)) return false;
			}
		}
        
        return answer;
    }
}
```

※ startsWith메소드 참고

https://blog.naver.com/5550304/222211608897




### 다른 풀이
1. sort를 이용한 풀이
    ```java
    import java.util.*;
    class Solution{
        public boolean solution(String[] phone_book) {
            boolean answer = true;
            Arrays.sort(phone_book);
            for (int i=0; i<phone_book.length-1; i++) {
                if (phone_book[i+1].startsWith(phone_book[i]))  return false;
            }
            return answer;
        }
    }
    ```
    - 설명

        phone_book 배열이 있을 때, String을 sort하면 아래와 같이 정렬된다.
        ```java
        String[] phone_book = {"123","9", "456", "789","00","98"};
        [00, 123, 456, 789, 9, 98] //sort 결과
        ```
        1. 이러한 성질을 이용해 배열을 sort한다.

        2. [i]를 prefix라고 생각하고, [i+1]가 [i]로 시작하는지 (접두어 인지) 검사한다.

        3. 만약 2번의 조건이 충족한다면, flase를 return해준다.
    
---
### 문제2

### 문제 설명
2차원 배열 clothes가 주어질 때, 서로 다른 옷의 조합의 수를 return한다.

### 풀이
1. 위장 종류와 갯수를 hashMap에 put한다.

    - 초기에 (위장 종류, 1)로 put

    -  map에 이미 위장 종류가 있다면, 위장 종류의 value를 꺼내와서 ++한 뒤, (위장 종류, value++)을 put

2. map size==1일 때, clothes의 길이를 return

    - 1번에서 map에 중복 저장하지 않으니, 위장 종류가 하나라면 map size가 1임

​

3. 경우의 수를 count한다 ( 옷의 갯수 + 안입을 경우)

    - 옷의 갯수 = value , 안입을 경우 = 1 


4. (모두 안입는 경우는 없으니) -1한 뒤 return


    ```java
    import java.util.*;

    class Solution {
        public int solution(String[][] clothes) {
            int answer=1;
            HashMap<String,Integer> map = new HashMap<String, Integer>();

            /*첫 번째*/
            for(int i=0; i<clothes.length; i++) {
                if(map.containsKey(clothes[i][1])) {
                    int temp=map.get(clothes[i][1]);
                    map.put(clothes[i][1], ++temp);
                }
                else map.put(clothes[i][1], 1);
            }

        /*두 번째*/       
        if(map.size()==1) return clothes.length;
            
            /*세 번째*/
        for (String key : map.keySet()) {
                answer = answer * (map.get(key) + 1);
            }

            /*네 번째*/
            return answer-1;
        }
    }
    ```
※ map.keySet(), map.get()을 이용해 value를 꺼내오는 방법이 성능 저하가 크다고 한다.


- Map에서 반복문을 사용하는 방법

https://blog.naver.com/5550304/222245480042


### 다른 풀이
1. getOrDefault 메소드를 사용한 풀이

- 찾는 키가 존재한다면, 찾는 키의 값을 반환하고, 없다면 기본 값을 반환한다.

- map.put( 키, 값)

    여기서 사용된 방법 : ( clothes[i][1]= 키, 키 값이 존재하면 키의 값을 넣어주고 없다면 0) +1

    ```java
    public int solution(String[][] clothes) {
        int answer = 1;
            Map<String, Integer> clothesMap = new HashMap<>(); 
            for (int i = 0; i < clothes.length; i++) {
                clothesMap.put(clothes[i][1], clothesMap.getOrDefault(clothes[i][1], 0)+1);
            }
            
            for (int val : clothesMap.values()){ // map에 저장된 모든 value 객체를 반환한다
                answer *= (val+1);
            }

            return answer-1;
        }
    ```

2. Iterator를 사용해 value를 꺼내오는 방법

    Iterator 인터페이스를 사용할 수 없는 컬랙션인 Map에서 Iterator 인터페이스를 사용하기 위해서는 Map에 entrySet(), KeySet() 메소드를 사용하여 Set객체를 반환받은 후, Iterator 인터페이스를 사용한다.

    ```java
    import java.util.HashMap;
    import java.util.Iterator;
    class Solution {
        public int solution(String[][] clothes) {
            int answer = 1;
            HashMap<String, Integer> map = new HashMap<>();
            for(int i=0; i<clothes.length; i++){
                String key = clothes[i][1];
                if(!map.containsKey(key)) {
                    map.put(key, 1);
                } else {
                    map.put(key, map.get(key) + 1);
                }
            }
            Iterator<Integer> it = map.values().iterator();
            while(it.hasNext()) {
                answer *= it.next().intValue()+1;
            }
            return answer-1;
        }
    }

    ```

### 삽질
처음에 모든 경우의 수를 구해서 hashset에 add하려고 했는데, 이렇게 구하다보면 위장 종류가 3개 이상일 때를 count하지 못한다.

```java
int answer = clothes.length;
HashSet<String> hs = new HashSet<String>();

for(int i=0; i<clothes.length-1; i++) {
		for(int j=i+1; j<clothes.length; j++) {        		
			if(!clothes[i][1].equals(clothes[j][1])) hs.add(clothes[i][0]+clothes[j][0]);
		}
}
		
answer+=hs.size();
```
