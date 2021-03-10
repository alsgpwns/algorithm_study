# Day18 [백준/2003번/투포인터]
## 문제
<https://www.acmicpc.net/problem/2003>


## 문제 설명
수들의 합2

N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

​

- 입력

    첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

​

- 출력

    첫째 줄에 경우의 수를 출력한다.





## 이해
![image](https://user-images.githubusercontent.com/45223821/110648896-7800eb80-81fc-11eb-8787-4b446ee02bb7.png)


​

본 문제에서 모든 경우의 수를 수행한다면(BruteForce), O(N^2)의 시간 복잡도를 가지기 때문에 시간초과가 발생하게된다.

또한 이 문제는 입력의 크기가 10,000이 넘으므로 nlongn또는 n의 알고리즘을 찾아야했다.

따라서 O(N)으로 시간복잡도를 줄여야 한다.

연속된 수열에 대한 합을 찾는 문제이기 때문에 two pinters 탐색을 이용할 수 있다.


## 풀이
1. sum<m : end인덱스를 한칸 늘려주고, sum에 값을 추가한다.

2. sum=m : end인덱스를 한칸 늘려주고, sum에 값을 추가한 뒤, cnt++

3. sum>m : sum에서 값을 빼고, start 인덱스를 한칸 늘려준다.


```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);    
		int len = sc.nextInt();
        long m = sc.nextLong();
        int[] arr = new int[len];
        long sum=0;
        int cnt=0;
        int s=0, e=0;
        for (int i = 0; i <len ; i++) {
            arr[i] =  sc.nextInt();
        }
        while(true) {
			if(sum >= m ) { // sum >= m
				sum = sum - arr[s++];
 			} else if(e >= len) {
				break;
			}
			else {  // sum < m
				sum = sum + arr[e++];
			}
			if(sum == m) {
				cnt++;
			}
			
		}
        
        System.out.println(cnt);
    }
}
```
## 다른 풀이
```java
  int cnt=0;
		int s = 0;
		int e = 0;
		int sum = 0;
		
		while(e<len) {
			while(e<len && sum<m) {
				sum = sum + arr[e];
				e++;
			}
			if(sum == m) cnt++;
			sum = sum - arr[s];
			s++;
		}
		return cnt;
```

## Ref
1. https://maivve.tistory.com/223

2. https://blog.naver.com/5550304/222269796696

3. https://blog.naver.com/kks227/220795165570 (문제 입출력예 설명)