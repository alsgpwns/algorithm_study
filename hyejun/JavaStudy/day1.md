# Day1 [HashSet]

 ![ttt](https://user-images.githubusercontent.com/45223821/105446092-bf670300-5cb4-11eb-97df-694fd4b6fca9.PNG)
 https://programmers.co.kr/learn/courses/30/lessons/68644


### 풀이
  
  * 중복 제거를 보다 쉽게하기 위해 HashSet을 이용했다.
  1. 이중 for문을 이용해 [i]와 [j]를 더한 값을 HashSet에 add한다.
  2. HashSet의 size를 answer배열의 크기로 초기화 한다.
  3. HashSet의 Index를 answer배열에 순차적으로 대입한다.
  4.  answer배열을 sort(오름차순 정렬)한다.

    ```java
    import java.util.*;
    class Solution {
        public int[] solution(int[] numbers) {
            HashSet<Integer> hs = new HashSet<Integer> ();
            int k=0;

            for(int i=0;i<numbers.length-1; i++)
            {
                for(int j=i+1; j<numbers.length; j++)
                {
                    hs.add(numbers[i]+numbers[j]);
                }
            }
            int[] answer = new int[hs.size()];
            for(Integer i:hs)
            {
                answer[k]=i;
                k++;
            }
            Arrays.sort(answer);
            return answer;
        }
    }
    ```

### 다른 풀이
*  내가 사용한 for:each문을 (hashSet의 Index를 배열에 저장하는 코드를)
* Iterator를 이용해 아래와 같이 사용할 수 있다.
* Iterator를 int형으로 형변환하여 answer배열에 넣을 수 있다.
```java
   Iterator itor = sumNumber.iterator();
        while(itor.hasNext()){
            answer[k] = (int)itor.next();
            k++;
        }
```
* Ref
    1. HashSet https://www.w3schools.com/java/java_hashset.asp
    2. ForEach https://www.geeksforgeeks.org/for-each-loop-in-java/

* 블로그
    * https://blog.naver.com/5550304/222211953831