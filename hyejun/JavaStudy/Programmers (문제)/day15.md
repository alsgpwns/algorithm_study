# Day15 [Leve2/greedy]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/109821851-bedd6700-7c79-11eb-8801-f5d69830c203.png)

<https://programmers.co.kr/learn/courses/30/lessons/42885>

### 문제 설명
한번에 최대 2명밖에 탈 수 없고, 무게 제한이 있는 구명보트가 있다.

구명보트를 최대한 적게 사용해 모든 사람들을 구출하려고 한다.

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/109821907-cd2b8300-7c79-11eb-8a5a-f600d67c1cff.png)


### 풀이
1. people배열을 sort한다.

2. 앞뒤로 더해서 limit보다 작거나 같다면, answer ++, i++(앞), k--(뒤)

3. 아니라면 answer++, k--(뒤)

    2번 조건을 충족하지 않았을 때, 배열의 뒷부분을 --
```java
import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int i=0;
        int k=people.length-1;
        Arrays.sort(people);
        
       while(i<=k) {
        	if(people[i]+people[k] <= limit) {
        		answer++;
        		i++;
        		k--;
        	}  else {
        		answer++;
        		k--;
        	}
        }
        
        return answer;
    }
}
```
### 다른 풀이
```java
import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        for (; i < j; --j) {
            if (people[i] + people[j] <= limit)
                ++i;
        }
        return people.length - i;
    }
}
```

### 삽질
1. 맨 앞과 맨 뒤를 더해서 조건식을 판별하고, ( [i] + [k] )

2. 양옆을 먼저 더해서 조건식을 판별한다. ( [i]+ [i+1] )

3. 아니라면, k를 -- 해준다. (맨 뒤를 --)

​

여기서 반례는 아래와 같다.

    [10 10 60 60 60 60 70], 70 일 때

    최적해는(70), (60, 10), (60, 10), (60), (60) → 5

    내가 푼 풀이의 해는 (10, 10) (60) (60) (60) (60) (70) → 6

​

처음엔 조건문을 더 꼼꼼히 짰다고 생각했는데, 이게 독이될줄은 몰랐다. ㅠ___ㅠ
```java
import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int i=0;
        int k=people.length-1;
        Arrays.sort(people);
        
       while(i<=k) {
        	if(people[i]+people[k] <= limit) {
        		answer++;
        		i++;
        		k--;
        	}  else if(people[i]+people[i+1] <= limit){
        		answer++;
        		i+=2;
        	} else {
        		answer++;
        		k--;
        	}
        
        return answer;
    }
}
```