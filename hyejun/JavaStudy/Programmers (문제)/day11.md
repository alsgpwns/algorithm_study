# Day11 [Level2]
![image](https://user-images.githubusercontent.com/45223821/107854769-8b20d580-6e61-11eb-86dd-f0fbaaa3564a.png)

<https://programmers.co.kr/learn/courses/30/lessons/43165>



### 문제1
재귀가 너무 어려워서 아래의 풀이를 참고했다.

아래의 풀이에서는 'bfs'라고 나와있지만, 이 풀이는 dfs이다.


bfs는 보통 큐를 쓰는데, 이유가 같은 레벨에서 +한번, -한번 연산한다.

하지만 이 풀이는 깊이를 우선적으로 탐색해서, +쪽으로 우선 쭉 가보고, 마지막까지 갔으면 하나 빼서 -하나 가보고, 이런식으로 반복하기 때문에 dfs이다.

<https://velog.io/@jaesika/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-DFS-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84>

### 문제 설명
배열 numbers의 정수를 받아, 이 수를 적절히 더하거나 빼서 'target number'를 만든다.


### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/107854791-b4d9fc80-6e61-11eb-823f-df6df2d237e3.png)

```java
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```
### 풀이
- [전체적인 알고리즘]

    dfs함수를 호출하며 매개변수로 numbers의 0번쨰 숫자와 다음 index인 1로 호출한다. 인덱스 i가 number.length와 같다면, 리프노드까지 탐색한것이기 때문에 target숫자와 같은지 확인하고 같으면1을, 아니면 0을 반환하여 count한다.


    ```java
    class Solution {
        public int solution(int[] numbers, int target) {
            int answer = 0;
            
            answer = dfs(numbers, target, numbers[0], 1) + dfs(numbers, target, -numbers[0], 1);
            
            return answer;
        }
        
        public int dfs(int[] numbers, int target, int sum, int i) {
            
            if(i == numbers.length) {
                if(sum == target) {
                    return 1;
                } else {
                    return 0;
                }
            }
            
            int result = 0;
            result += dfs(numbers, target, sum+numbers[i], i+1); //  sum+numbers[i]: 바로 뒤 index랑 더해줌
            result += dfs(numbers, target, sum-numbers[i], i+1); //  sum+numbers[i]: 바로 뒤 index랑 빼줌
            return result;
        }
    }
    ```

- [Test case]
  풀이 디버깅만 20번은 넘게 해본것같다. 하지만 아직도 이 코드가 어떻게 완전탐색이 되는건지 이해가 잘 가지않아, test case를 넣어 출력해보았다


    1. int[] numbers= {1,2,3};
    (-가 붙지 않은 값들은 +이다)
    ![image](https://user-images.githubusercontent.com/45223821/107854821-e6eb5e80-6e61-11eb-8271-a5a2e22717a8.png)



    2. int[] numbers= {1,1,1,1,1};
    dfs를 +로 호출하는곳은(첫번째 dfs) +로 표시
    dfs를 -로 호출하는곳은(두번째 dfs) -로 표시
    ![image](https://user-images.githubusercontent.com/45223821/107854837-fb2f5b80-6e61-11eb-88b3-7fa62b4a9393.png)
