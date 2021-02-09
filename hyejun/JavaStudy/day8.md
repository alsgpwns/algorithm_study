# Day [Level]
### 문제1
![image](https://user-images.githubusercontent.com/45223821/106986391-9c594a80-67ae-11eb-880e-faee1e6551a6.png)


<https://programmers.co.kr/learn/courses/30/lessons/68644>
### 문제 설명
numbers 배열이 주어지고, 배열의 자기 자신을 제외한 Index끼리 모두 더한다.

더한 후, 중복되는 값을 제거하고, 오름차순으로 정렬을 한 배열을 return해준다.

### 입출력 예
```java
// 1번
numbers =[2,1,3,4,1]
result =[2,3,4,5,6,7]

// 2번
numbers = [0,100,1,15,14]
result =[1, 14, 15, 16, 29, 100, 101, 114, 115]
```
### 풀이
중복 제거를 보다 쉽게 하기 위해 HashSet을 이용했다.
​

1. 이중 for문을 이용해 [i]와 [j]를 더한 값을 HashSet에 add한다.

2. HashSet의 size를 answer배열의 크기로 초기화 한다.

3. HashSet의 Index를 answer배열에 순차적으로 대입한다.

4. answer배열을 sort(오름차순 정렬)한다.
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
hashSet의 Index를 배열에 저장하는 코드를, (내가 푼 코드)

```java
    for(Integer i:hs)
    {
        nswer[k]=i;
        k++;
    }
```
Iterator를 이용해 아래와 같이 대입하는 코드로 변경할 수 있다.

Iterator를 int형으로 형변환 하여 answer배열에 넣을 수 있다.
```java
    Iterator itor = sumNumber.iterator();
        while(itor.hasNext()){
            answer[k] = (int)itor.next();
            k++;
        }
```
---
### 문제2
![image](https://user-images.githubusercontent.com/45223821/106986983-decf5700-67af-11eb-8e51-7aabe42c2abf.png)

<https://programmers.co.kr/learn/courses/30/lessons/64061>

### 입출력 예
![image](https://user-images.githubusercontent.com/45223821/106986951-ceb77780-67af-11eb-80bf-8787279e0099.png)

### 풀이
아쉬운점

1. list - remove 는 문제의도와 100% 부합하는것 같진 않음 실제 프로그램이라면 list-remove를 사용했을 때, 게임이 종료된 후 삭제되는 효과를 볼 수 있을것같고 stack-pop을 사용했을 떄, 게임 중에서도 삭제되는 효과를 볼 수 있을것같다.

2. class를 따로 뺐는데 그닥 효율적인것 같진 않음

```java
import java.util.LinkedList;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        LinkedList<Integer> list = new LinkedList<Integer>();
        Count list_num= new Count();
        
        for(int i=0;i<moves.length;i++)
        {
            int mNum=moves[i]-1;
            int j=0;

            while(j<board.length-1 && board[j][mNum]==0)
            {
                j++;
            }
            if(board[j][mNum]!=0)
            {
                list.add(board[j][mNum]);
                board[j][mNum]=0;
            }
        }
        for(int i=0;i<30;i++)
        {
            answer =list_num.countAnswer(list, answer);
        }

        return answer;
    }
}
    
class Count{
	  public int countAnswer(LinkedList<Integer> list,int answer) {
		  
		  for(int k=1;k<list.size();k++)
          {
              if(list.get(k)==list.get(k-1))
              {
                  list.remove(k);
                  list.remove(k-1);
                  answer+=2;
              }
          }
	        
		  return answer;
	  }
}

```
### 다른 풀이
```java
import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int move : moves) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][move - 1] != 0) {
                    if (stack.isEmpty()) {
                        stack.push(board[j][move - 1]);
                        board[j][move - 1] = 0;
                        break;
                    }
                    if (board[j][move - 1] == stack.peek()) {
                        stack.pop();
                        answer += 2;
                    } else
                        stack.push(board[j][move - 1]);
                    board[j][move - 1] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}

```
---
### 문제3[In progress]
실패율

<https://programmers.co.kr/learn/courses/30/lessons/42889>
### 문제 설명

### 풀이
코드 복잡도 생각 안하고, 리팩토링할 생각으로 풀고있는데, 애초에 풀이를 잘못짠것같다.
다시 생각해야될듯
```java
import java.util.*;
import java.util.Map.Entry;
class Solution {
    public int[] solution(int N, int[] stages) {
       int[] answer = new int[N];
	    int count=0;
		double num=stages.length;
        Map<Integer, Double> map = new HashMap<Integer,Double>();
		for(int i=1;i<N+1;i++) map.put(i, 0.0);
		Arrays.sort(stages);
        int j=1;
        for(int i=0; i<stages.length-1; i++) { //이 부분이 문제
			if(stages[i]==j) {
				count++;      
			}
			if(stages[i+1]!=j && count!=0) {
				map.put(j, count/num);
				num=num-count;
				count=0;
				j++;
			}
		}
		if(j==1) map.put(stages[0],1.0);
        List<Entry<Integer, Double>> list_entries = new ArrayList<Entry<Integer, Double>>(map.entrySet());

		// 비교함수 Comparator를 사용하여 내림 차순으로 정렬
		Collections.sort(list_entries, new Comparator<Entry<Integer, Double>>() {
			// compare로 값을 비교
			public int compare(Entry<Integer, Double> obj1, Entry<Integer, Double> obj2)
			{
				// 내림 차순으로 정렬
				return obj2.getValue().compareTo(obj1.getValue());
			}
		});
        int k=0;
		for(Entry<Integer, Double> entry : list_entries) {
			answer[k++]=entry.getKey();
		}
        return answer;
    }
}
```

---
### 문제4[In progress]
비밀지도

<https://programmers.co.kr/learn/courses/30/lessons/17681>
