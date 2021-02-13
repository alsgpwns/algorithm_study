# DFS (깊이 우선 탐색)

### 그래프
- 그래프
 
    정점과 간선으로 이루어진 자료구조의 일종
    
    G=(V,E)

​

- 그래프 탐색
  
    하나의 정점으로부터 시작하여 차례대로 모든 정점을 한번씩 방문하는것
    ex) 특정 도시에서 다른 도시로의 이동 여부 판별 or 회로에서 단자와 단자의 연결 여부 확인등



### DFS (깊이 우선 탐색)
- 깊이 우선 탐색의 개념
  
    루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
    즉, 다음 노드로 넘어가기 전에 해동 노드의 분기에 대해 완전 탐색하는 방식

    1. 미로를 탐색할 때, 한 방향으로 갈 수 있을 때 까지 계속 가다가 더이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서, 이곳부터 다른 방향으로 다시 탐색을 진행하는 방법과 유사
    2. 넓게(wide) 탐색하기 전에 깊게(deep) 탐색한다
    3. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택한다
    4. 깊이 우선 탐색이 너비 우선 탐색보다 조금 간단하다
    5. 검색속도는 너비 우선 탐색(BFS)에 비해 느리다



-  깊이 우선 탐색의 특징

   1. 자기 자신을 호출하는 순환 알고리즘의 형태를 지닌다.

   2. 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야한다. (검사하지 않을 경우 무한루프에 빠질 위험이 있음)


- 장점

    1. 구현이 너비 우선 탐색보다 간단하다

    2. 현재 경로상의 노드들만 기억하면 되므로, 저장 공간의 수요가 비교적 적다.

    3.  목표 노드가 깊은 단계에 있는 경우 해를 빨리 구할 수 있다.



- 단점

1. 단순 검색 속도는 너비 우선 탐색보다 느리다.

2. 해가 없는 경우에 빠질 가능성이 있다. (이러한 경우 사전에 임의의 깊이를 지정한 후 탐색하도록 하고, 목표 노드를 발견하지 못할 경우 다음 경로를 탐색하도록 한다.)

3. 목표에 이르는 경로가 다수인 경우 (복잡한 경우) 구한 해가 최적이 아닐 수 있다.



![image](https://user-images.githubusercontent.com/45223821/107854941-c079f300-6e62-11eb-86d6-8bb404e4ccdc.png)


![image](https://user-images.githubusercontent.com/45223821/107854949-ca035b00-6e62-11eb-932a-8979c1cbbed5.png)

​

### 깊이 우선 탐색의 시간 복잡도
1. DFS는 그래프 (정점 N, 간선 E)의 모든 간선을 조회한다.
2. 인접 리스트로 표현된 그래프 : O(N+E)
3. 인접 행렬로 표현된 그래프: O(N^2)


### 인접 리스트를 이용한 DFS 구현
```java
import java.util.*;

public class DFS_List {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 정점의 개수 
		int m = sc.nextInt(); // 간선의 개수 
		int v = sc.nextInt(); // 탐색을 시작할 정점의 번호 

		boolean visited[] = new boolean[n + 1]; // 방문 여부를 검사할 배열 

		LinkedList<Integer>[] adjList = new LinkedList[n + 1];

		for (int i = 0; i <= n; i++) {
			adjList[i] = new LinkedList<Integer>();
		}

		// 두 정점 사이에 여러 개의 간선이 있을 수 있다.
		// 입력으로 주어지는 간선은 양방향이다.
		for (int i = 0; i < m; i++) {
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();
			adjList[v1].add(v2);
			adjList[v2].add(v1);
		}

		for (int i = 1; i <= n; i++) { // 방문 순서를 위해 오름차순 정렬 
			Collections.sort(adjList[i]);
		}

		System.out.println("DFS - 인접리스트");
		dfs_list(v, adjList, visited);
	}
	
	// DFS - 인접리스트 - 재귀로 구현 
	public static void dfs_list(int v, LinkedList<Integer>[] adjList, boolean[] visited) {
		visited[v] = true; // 정점 방문 표시
		System.out.print(v + " "); // 정점 출력

		Iterator<Integer> iter = adjList[v].listIterator(); // 정점 인접리스트 순회
		while (iter.hasNext()) {
			int w = iter.next();
			if (!visited[w]) // 방문하지 않은 정점이라면 
				dfs_list(w, adjList, visited); // 다시 DFS
		}
	}

```

![image](https://user-images.githubusercontent.com/45223821/107854966-df788500-6e62-11eb-8001-7a35c0edb083.png)
- 입출력 예

    ```java
    // 입력
    5 5 1
    5 4
    5 2
    1 2
    3 4
    3 1

    //출력
    DFS - 인접리스트
    1 2 5 4 3 
    ```

    ```java
    // 입력
    5 5 3
    5 4
    5 2
    1 2
    3 4
    3 1

    //출력
    DFS - 인접리스트
    3 1 2 5 4 
    ```

     
  

### 인접 행렬로 구현한 DFS

```java
import java.util.*;

public class DFS_Array {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 정점의 개수 
		int m = sc.nextInt(); // 간선의 개수 
		int v = sc.nextInt(); // 탐색을 시작할 정점의 번호 

		boolean visited[] = new boolean[n + 1]; // 방문 여부를 검사할 배열 

		int[][] adjArray = new int[n+1][n+1];

		// 두 정점 사이에 여러 개의 간선이 있을 수 있다.
		// 입력으로 주어지는 간선은 양방향이다.
		for(int i = 0; i < m; i++) {
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();

			adjArray[v1][v2] = 1;
			adjArray[v2][v1] = 1;
		}

		System.out.println("DFS - 인접행렬 / 재귀로 구현");
		dfs_array_recursion(v, adjArray, visited);
		Arrays.fill(visited, false); // 스택 DFS를 위해 visited 배열 초기화

		System.out.println("\n\nDFS - 인접행렬 / 스택으로 구현");
		dfs_array_stack(v, adjArray, visited, true);
	}
	
	//DFS - 인접행렬 / 재귀로 구현 
	public static void dfs_array_recursion(int v, int[][] adjArray, boolean[] visited) {
		int l = adjArray.length-1;
		visited[v] = true;
		System.out.print(v + " ");

		for(int i = 1; i <= l; i++) {
			if(adjArray[v][i] == 1 && !visited[i]) {
				dfs_array_recursion(i, adjArray, visited);
			}
		}
	}

	//DFS - 인접행렬 / 스택으로 구현 
	public static void dfs_array_stack(int v, int[][] adjArray, boolean[] visited, boolean flag) {
		int l = adjArray.length-1;
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(v);
		visited[v] = true;
		System.out.print(v + " ");

		while(!stack.isEmpty()) {
			int w = stack.peek();
			flag = false; 

			for(int i = 1; i <= l; i++) {
				if(adjArray[w][i] == 1 && !visited[i]) {
					stack.push(i);
					System.out.print(i + " ");
					visited[i] = true;
					flag = true;
					
					break;
				}
			}

			if(!flag) {
				stack.pop();
			}
		}
	}
	
}
```

![image](https://user-images.githubusercontent.com/45223821/107855003-21a1c680-6e63-11eb-91f7-2a7b45ce0c17.png)

- 입출력 예
  ```java
    //입력
    4 5 3
    1 2
    1 3
    1 4
    2 4
    3 4

    //출력
    DFS - 인접행렬 / 재귀로 구현
    3 1 2 4 

    DFS - 인접행렬 / 스택으로 구현
    3 1 2 4 
  ```

  ```java
    //입력
    4 5 1
    1 2
    1 3
    1 4
    2 4
    3 4

    //출력
    DFS - 인접행렬 / 재귀로 구현
    3 1 2 4 

    DFS - 인접행렬 / 스택으로 구현
    3 1 2 4 
  ```

#### Ref
  1. https://yunyoung1819.tistory.com/86
  2. https://freestrokes.tistory.com/88
  3. SW Expert Academy
  4. https://minhamina.tistory.com/22 (DFS)
