# Day [Level]
<https://programmers.co.kr/learn/courses/30/lessons/42883>


## 문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 한다.

​![image](https://user-images.githubusercontent.com/45223821/109332453-7997ee80-78a1-11eb-9fdd-3f4d0f217328.png)


예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 이다.


중요한 점은 "가장 큰 수"가 아닌 "k개의 수를 제거했을 떄 얻을 수 있는 가장 큰 수"이다.



## 풀이
greedy는 처음 방법을 찾는게 어려운것같다.

1. 앞 숫자와 뒷 숫자를 비교하며, 뒷 숫자가 더 크다면 앞 숫자를 삭제한다.

    1-1. 1번을 k번 반복한다.

2. 1번을 실행하지 않은 경우, index 0부터 len-1까지 끊어 return한다.

    ex. number = 3111, k=2 : return = 31

    ```java
    import java.util.*;
    class Solution {
        public String solution(String number, int k) {
            StringBuilder ans = new StringBuilder(number);
            String answer = "";
            
            while (k > 0) {
                int len = ans.length();
                boolean removed = false;
                for (int i = 0; i < len - 1; i++) {
                    if (ans.charAt(i) < ans.charAt(i + 1)) {
                        ans.deleteCharAt(i);
                        removed = true;
                        break;
                    }
                }
            if (!removed) {
                    answer = ans.substring(0, len - 1);
                return answer;
                }
                k--;
            }
            answer = ans.toString();
            return answer;
        }
    }
    ```
## 다른 풀이
생각한 알고리즘은 비슷하고, 구현 방법(stack)에서 차이점을 보인다.

​

   1. (처음 한번) i를 stack에 넣는다.

   2. i와  i+1을 비교한 후, 작은 숫자를 stack에서 꺼낸다. (삭제)

   3. 비교한 큰 수를 stack에 넣는다.

        3-1. 2~3을 k번 반복한다.

   4. 가장 큰 수를 넣은 stack을 배열에 대입한 후, String형으로 변환 하고, return해준다.
   
        ```java
        import java.util.Stack;
        class Solution {
            public String solution(String number, int k) {
                char[] result = new char[number.length() - k];
                Stack<Character> stack = new Stack<>();

                // charAt으로 비교하고, stack에 넣어줌
                for (int i=0; i<number.length(); i++) {
                    char c = number.charAt(i);
                    while (!stack.isEmpty() && stack.peek() < c && k-- > 0) {
                        stack.pop();
                    }
                    stack.push(c);
                }
                
                // stack에서 value를 get한 후, char 배열에 넣어줌
                for (int i=0; i<result.length; i++) {
                    result[i] = stack.get(i);
                }
                return new String(result);
            }
        }
        ```


## 삽질
초반에 String bilder를 사용하지 않고 String으로 SubString연산을 했었는데, String 특성상 (불변) 계속 new 연산으로 객체를 생성하며, 이 부분에서 시간을 많이 잡아먹고 에러가 났었다.

(같은 알고리즘을 C++로 짰을 땐 돌아감)

위의 풀이처럼 Stirng Builder로 짰을 땐(과도한 new연산을 하지 않으니) 잘 돌아간다.

```java
class Solution {
    public String solution(String number, int k) {
        String ans = number;
        while (k > 0) {
            int len = ans.length();
            boolean removed = false;
            for (int i = 0; i < len - 1; i++) {
                if (ans.charAt(i) < ans.charAt(i + 1)) {
                    ans = ans.substring(0, i) + ans.substring(i + 1);
                    removed = true;
                    break;
                }
            }
            if (!removed) {
                ans = ans.substring(0, len - 1);
            }
            k--;
        }
        return ans;
    }
}
```


## Ref
1. https://www.tutorialspoint.com/converting-a-stringbuilder-to-string-in-java (StringBuilder to String)

2. https://codevang.tistory.com/121 (StringBuilder Method)

3. http://www.tcpschool.com/java/java_api_string (String 불변 특징)